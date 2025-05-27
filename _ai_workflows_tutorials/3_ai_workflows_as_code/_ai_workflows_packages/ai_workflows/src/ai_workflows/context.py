"""Manages information sources and retrieval for AI workflows.

This module is like a smart library system that:
- Collects information from files, folders, and websites
- Breaks long texts into smaller, manageable pieces
- Finds relevant information when needed
- Keeps track of what's most important

Uses a specialized database (Qdrant) to make finding information fast and accurate.
"""

from enum import Enum
import logging
from pathlib import Path
import time
from typing import Any

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders.base import BaseLoader
from langchain_community.document_loaders import WebBaseLoader, TextLoader, DirectoryLoader
from langchain_core.embeddings import Embeddings
from langchain_qdrant import QdrantVectorStore
from pydantic import BaseModel, Field, field_validator
from qdrant_client.models import Distance, VectorParams
from qdrant_client import QdrantClient

from .constants import (
    DATA_DIR,
    DEFAULT_CHUNK_OVERLAP,
    DEFAULT_CHUNK_SIZE,
    DEFAULT_MAX_DOCS,
    DEFAULT_PRIORITY,
    GLOB_PATTERN,
    MAX_PRIORITY,
    MIN_PRIORITY,
    TEXT_SEPARATORS,
    WORKFLOW_DIR
)

logger = logging.getLogger(__name__)


class ContextLoadError(Exception):
    """Error raised when we can't load information from a source."""
    pass


class ContextSourceType(str, Enum):
    """Types of places where we can get information from.

    Types:
    - FILE: A single document (like a text file)
    - FOLDER: A collection of documents in one place
    - URL: A webpage on the internet
    """
    FILE = 'file'
    FOLDER = 'folder'
    URL = 'url'


class ContextSource(BaseModel):
    """Instructions for where and how to get information.

    Example:
        ```yaml
        documentation:
          type: "folder"          # What kind of source
          path: "./docs"          # Where to find it
          priority: 3             # How important (1-5)
          metadata:               # Extra details
            category: "technical"
        ```

    Attributes:
        type: Kind of source (file/folder/URL)
        path: Where to find it
        priority: How important it is (1-5, higher = more important)
        metadata: Extra details about the source
    """
    type: ContextSourceType
    path: str
    priority: int = Field(default=DEFAULT_PRIORITY, ge=MIN_PRIORITY, le=MAX_PRIORITY)
    metadata: dict[str, Any] = Field(default_factory=dict)

    @field_validator('path')
    @classmethod
    def validate_path(cls, v: str, info) -> str:
        """Checks if the file or folder exists."""
        type_value = info.data.get('type')
        if type_value in (ContextSourceType.FILE, ContextSourceType.FOLDER):
            path = Path(v)
            if not path.is_absolute():
                path = (WORKFLOW_DIR / path).resolve()
            if not path.exists():
                raise ValueError(f'Path does not exist: {path}')
            return str(path)
        return v


class WorkflowContextConfig(BaseModel):
    """Rules for handling information sources.

    Example:
        ```yaml
        sources:
          docs:                     # Local documents
            type: "folder"
            path: "./docs"
          website:                  # Online information
            type: "url"
            path: "https://example.com"
        max_docs_per_source: 5      # Limit per source
        chunk_size: 1000            # Characters per piece
        chunk_overlap: 200          # Overlap between pieces
        recreate_collection: false  # Start fresh?
        ```

    Attributes:
        sources: Where to get information from
        max_docs_per_source: How many documents to use from each source
        chunk_size: How big each piece should be
        chunk_overlap: How much pieces should overlap
        recreate_collection: Whether to start with a fresh database
    """
    model_config = {'extra': 'forbid'}

    sources: dict[str, ContextSource]
    max_docs_per_source: int = Field(default=DEFAULT_MAX_DOCS, ge=1)
    chunk_size: int = Field(default=DEFAULT_CHUNK_SIZE, ge=100)
    chunk_overlap: int = Field(default=DEFAULT_CHUNK_OVERLAP, ge=0)
    recreate_collection: bool = Field(default=False)


class WorkflowContext:
    """The system that manages all information for a workflow.

    Think of it as a smart assistant that:
    1. Gathers information from different places
    2. Organizes it into easy-to-handle pieces
    3. Quickly finds what you need when you ask
    4. Remembers what's most important

    Example:
        ```python
        # Set up the system
        config = WorkflowContextConfig(
            sources={'docs': ContextSource(type='folder', path='./docs')},
            max_docs_per_source=5
        )
        context = WorkflowContext(config, embeddings_model)

        # Get it ready and load information
        context.setup('my_workflow')
        context.load_all()

        # Find relevant information
        info = context.get_relevant('How do I start?', 'docs')
        ```
    """

    def __init__(self, config: WorkflowContextConfig, embeddings: Embeddings):
        """Sets up the context manager.

        Args:
            config: Information handling settings
            embeddings: Model for finding similar texts
        """
        self._config = config
        self._embeddings = embeddings
        self._store = None
        self._splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.chunk_size,
            chunk_overlap=config.chunk_overlap,
            separators=TEXT_SEPARATORS,
            keep_separator=True
        )
        self._client = None
        self._collection_path = None

    def _collection_exists(self, workflow_key: str) -> bool:
        """Checks if database exists for this workflow.

        Args:
            workflow_key: Workflow name

        Returns:
            True if exists, False otherwise
        """
        try:
            collections = self._client.get_collections().collections
            return any(c.name == workflow_key for c in collections)
        except Exception:
            return False

    def setup(self, workflow_key: str) -> None:
        """Prepares system for a new workflow.

        Args:
            workflow_key: Workflow name

        Raises:
            ContextLoadError: If database setup fails
        """
        try:
            self._collection_path = DATA_DIR / workflow_key
            self._collection_path.parent.mkdir(parents=True, exist_ok=True)

            logger.info(f'Setting up vector store in: {self._collection_path}')

            self._client = QdrantClient(
                path=str(self._collection_path),
                force_disable_compression=True
            )

            # Check if database exists and has information
            if self._collection_exists(workflow_key):
                collection_info = self._client.get_collection(workflow_key)
                logger.info(f'Found existing collection with {collection_info.points_count} documents')

            if self._config.recreate_collection or not self._collection_exists(workflow_key):
                logger.info(f'Creating new collection {workflow_key}')
                test_embedding = self._embeddings.embed_query('test')
                embedding_size = len(test_embedding) if isinstance(test_embedding, list) else test_embedding.shape[0]

                self._client.recreate_collection(
                    collection_name=workflow_key,
                    vectors_config=VectorParams(
                        size=embedding_size,
                        distance=Distance.COSINE
                    )
                )

            self._store = QdrantVectorStore(
                client=self._client,
                collection_name=workflow_key,
                embedding=self._embeddings
            )
            logger.info('Vector store setup complete')
        except Exception as e:
            raise ContextLoadError(f'Failed to setup vector store: {str(e)}') from e

    def load_all(self) -> dict[str, str]:
        """Loads all configured sources.

        Returns:
            Status of each source's loading
        """
        results = {}
        logger.info(f'Loading {len(self._config.sources)} sources')

        for name, source in self._config.sources.items():
            try:
                logger.info(f'Loading source: {name} from {source.path}')
                self._load_source(name, source)
                # Verify documents were added
                collection_info = self._client.get_collection(self._store.collection_name)
                logger.info(f'Collection now has {collection_info.points_count} documents')
                results[name] = 'success'
            except Exception as e:
                logger.error(f'Failed to load source {name}: {str(e)}')
                results[name] = f'error: {str(e)}'
        return results

    def get_relevant(self, query: str, source_key: str | list[str]) -> str:
        """Finds information matching a query.

        Args:
            query: What to look for
            source_key: Where to look

        Returns:
            Relevant information as formatted text
        """
        try:
            from qdrant_client.http import models

            # Clean query for logging
            clean_query = ' '.join(query.split())
            logger.info(
                f'Searching context:\n'
                f'- Query: {clean_query[:100]}...\n'
                f'- Query length: {len(query):,} chars\n'
                f'- Sources: {source_key if isinstance(source_key, str) else ", ".join(source_key)}\n'
                f'- Max docs: {self._config.max_docs_per_source}'
            )

            # Set up search filter
            filter_condition = (
                models.Filter(
                    should=[
                        models.FieldCondition(
                            key='metadata.source',
                            match=models.MatchValue(value=sk)
                        ) for sk in source_key
                    ]
                ) if isinstance(source_key, (list, tuple)) else
                models.Filter(
                    must=[
                        models.FieldCondition(
                            key='metadata.source',
                            match=models.MatchValue(value=source_key)
                        )
                    ]
                )
            )

            # Search for relevant information
            start_time = time.time()
            docs = self._store.similarity_search_with_score(
                query,
                k=self._config.max_docs_per_source,
                filter=filter_condition
            )
            search_time = time.time() - start_time

            if not docs:
                logger.warning(
                    f'No matching documents found:\n'
                    f'- Query: {clean_query[:100]}...\n'
                    f'- Sources searched: {source_key}\n'
                    f'- Search time: {search_time:.3f}s'
                )
                return ''

            # Check quality of results
            scores = [score for _, score in docs]
            avg_score = sum(scores) / len(scores)

            logger.info(
                f'Search results overview:\n'
                f'- Found documents: {len(docs)}\n'
                f'- Search time: {search_time:.3f}s\n'
                f'- Best match: {max(scores):.1%}\n'
                f'- Average match: {avg_score:.1%}\n'
                f'- Weakest match: {min(scores):.1%}'
            )

            # Log detailed quality information
            logger.debug(
                'Search results quality assessment:\n' +
                '\n'.join(
                    f'- Match {i+1}:\n'
                    f'  • Relevance: {score:.1%} {"✓" if score > avg_score else "✗"}\n'
                    f'  • Source: {doc.metadata["source"]}\n'
                    f'  • Priority: {doc.metadata.get("priority", "N/A")}/5\n'
                    f'  • Content length: {len(doc.page_content):,} chars\n'
                    f'  • Preview: {" ".join(doc.page_content[:100].split())}...'
                    for i, (doc, score) in enumerate(docs)
                )
            )

            # Sort by importance and relevance
            sorted_docs = sorted(
                docs,
                key=lambda x: (-x[0].metadata.get('priority', 0), -x[1])
            )

            # Format the results
            formatted_docs = [
                f'## {doc.metadata.get("source", "UNKNOWN").upper()}\n\n{doc.page_content}\n'
                for doc, _ in sorted_docs
            ]
            combined_text = '\n\n---\n'.join(formatted_docs)

            # Log summary of results
            unique_sources = {doc.metadata["source"] for doc, _ in sorted_docs}
            logger.info(
                f'Final context assembly:\n'
                f'- Documents used: {len(formatted_docs)}\n'
                f'- Total size: {len(combined_text):,} chars\n'
                f'- Average chunk: {len(combined_text)/len(formatted_docs):,.0f} chars\n'
                f'- Sources used: {", ".join(sorted(unique_sources))}\n'
                f'- Source coverage: {len(unique_sources)}/{len(source_key) if isinstance(source_key, list) else 1}'
            )

            return combined_text

        except Exception as e:
            logger.error(
                f'Error retrieving relevant context:\n'
                f'- Error type: {type(e).__name__}\n'
                f'- Error message: {str(e)}\n'
                f'- Query: {clean_query[:100]}...\n'
                f'- Query length: {len(query):,} chars\n'
                f'- Sources: {source_key}',
                exc_info=True
            )
            return ''

    def _get_loader(self, source: ContextSource) -> BaseLoader:
        """Gets appropriate loader for source type."""
        if source.type == ContextSourceType.URL:
            return WebBaseLoader(
                web_paths=[source.path],
                verify_ssl=False
            )
        elif source.type == ContextSourceType.FILE:
            return TextLoader(str(Path(source.path)))
        elif source.type == ContextSourceType.FOLDER:
            return DirectoryLoader(
                str(Path(source.path)),
                glob=GLOB_PATTERN,
                loader_cls=TextLoader
            )
        raise ValueError(f'Unknown source type: {source.type}')

    def _load_source(self, name: str, source: ContextSource) -> None:
        """Loads a single source.

        Args:
            name: Source name
            source: Source configuration
        """
        try:
            # Log what we're doing
            logger.info(f'Loading source: {name} ({source.type}) from {source.path}')

            # Load the documents
            loader = self._get_loader(source)
            documents = loader.load()
            raw_size = sum(len(d.page_content) for d in documents)
            logger.info(
                f'Raw document metrics for {name}:\n'
                f'- Documents: {len(documents)}\n'
                f'- Total size: {raw_size:,} chars\n'
                f'- Average size: {raw_size/len(documents):,.0f} chars/doc'
            )

            # Break into chunks
            split_docs = self._splitter.split_documents(documents)
            split_size = sum(len(d.page_content) for d in split_docs)
            logger.info(
                f'Chunk metrics for {name}:\n'
                f'- Chunks: {len(split_docs)}\n'
                f'- Total size: {split_size:,} chars\n'
                f'- Average chunk: {split_size/len(split_docs):,.0f} chars\n'
                f'- Size ratio: {split_size/raw_size:.1%} of original'
            )

            # Add source information
            for doc in split_docs:
                doc.metadata = {
                    'source': name,
                    'priority': source.priority,
                    **source.metadata
                }

            if split_docs:
                logger.debug(
                    f'Sample chunk from {name}:\n'
                    f'- Size: {len(split_docs[0].page_content)} chars\n'
                    f'- Metadata: {split_docs[0].metadata}\n'
                    f'- Preview: {" ".join(split_docs[0].page_content[:200].split())}'
                )

            # Save to database
            before_count = self._client.get_collection(self._store.collection_name).points_count
            self._store.add_documents(split_docs)
            after_count = self._client.get_collection(self._store.collection_name).points_count

            logger.info(
                f'Vector store update for {name}:\n'
                f'- Previous docs: {before_count:,}\n'
                f'- Added docs: {len(split_docs):,}\n'
                f'- Current docs: {after_count:,}'
            )

        except Exception as e:
            logger.error(
                f'Failed to load source {name}:\n'
                f'- Error type: {type(e).__name__}\n'
                f'- Error message: {str(e)}'
            )
            raise
