<div align="center">
  <h1>Framework AI Workflows</h1>
  <p><i>Transformez vos instructions textuelles en code Python</i></p>
</div>

## Ce que fait ce framework

Ce framework vous aide à convertir vos workflows IA textuels en code Python. Il :
- prend vos instructions (dans un fichier YAML)
- configure les outils d'IA que vous choisissez
- exécute vos tâches en séquence
- sauvegarde les résultats dans des fichiers

## Exemple rapide

```python
from ai_workflows import Workflow

# Créez un workflow à partir de vos instructions
workflow = Workflow(
    config_path='config.yaml',      # Votre configuration d'outils IA
    instructions_path='tasks.yaml'  # Vos instructions de workflow
)

# Exécutez-le !
result = workflow.run()
```

## Composants principaux

### 1. Fichier d'instructions (tasks.yaml)
Définissez ce que vous voulez faire :
```yaml
goal: "Analyser les retours clients"
tasks:
  - key: 'extract_topics'
    description: 'Identifier les principaux sujets'
  - key: 'analyze_sentiment'
    description: 'Analyser le sentiment par sujet'
```

### 2. Fichier de configuration (config.yaml)
Choisissez vos outils d'IA :
```yaml
llm:
  type: "langchain_groq.ChatGroq"
  model_name: "llama-3.3-70b-versatile"

embeddings:
  type: "langchain_huggingface.HuggingFaceEmbeddings"
  model_name: "all-MiniLM-L6-v2"
```

## Installation

1. **Prérequis**
   - Python 3.10
   - Poetry (gestionnaire de paquets)

2. **Configuration**
   ```bash
   # Récupérez le code
   git clone https://github.com/cbardyn/ai-swiss-workflows
   cd _ai_workflows_packages/ai_workflows

   # Installez les dépendances
   poetry install

   # Activez l'environnement
   source .venv/bin/activate  # (ou .\.venv\Scripts\activate sous Windows)
   ```

3. **Configuration**
   ```bash
   # Ajoutez votre clé API
   echo "GROQ_API_KEY=votre-clé-ici" > .env
   ```

## Comment l'utiliser

### 1. Écrivez vos instructions
Créez `tasks.yaml` :
```yaml
goal: "Votre objectif de workflow"
tasks:
  - key: 'task_1'
    description: 'Ce qu'il faut faire'
    inputs:
      - from_context: ['un_fichier']
    outputs:
      - key: 'resultat'
        file: 'sortie.md'
```

### 2. Configurez les outils d'IA
Créez `config.yaml` :
```yaml
llm:
  type: "langchain_groq.ChatGroq"
  model_name: "llama-3.3-70b-versatile"
  temperature: 0  # Réponses plus précises
```

### 3. Exécutez votre workflow
```python
from ai_workflows import setup_logging, Workflow

# Configurez la journalisation (optionnel mais utile)
setup_logging()

# Créez et exécutez le workflow
workflow = Workflow('config.yaml', 'tasks.yaml')
result = workflow.run()
```

## Fonctionnalités du framework

### Gestion intelligente du contexte
```python
# Le framework automatiquement :
# - charge les fichiers et URLs
# - crée une base de données vectorielle consultable
# - trouve les informations pertinentes pour chaque tâche
```

### Orchestration des tâches
```python
# Le framework gère :
# - le séquençage des tâches
# - le passage d'informations entre les tâches
# - le suivi de la progression
```

### Gestion des erreurs
```python
# Gestion intégrée pour :
# - fichiers manquants
# - échecs d'API
# - configurations invalides
```

## Fonctionnalités que nous aimerions ajouter

- Plus de connecteurs vers des systèmes externes (Dropbox, Google Drive, etc.)
- Meilleurs tests : pas encore de tests automatisés pour garantir le bon fonctionnement
- Meilleure sécurité : les clés API sont stockées dans des fichiers texte simples
- Meilleures performances : les tâches s'exécutent l'une après l'autre au lieu d'en parallèle
- Meilleure fiabilité : pas de modèles IA de secours en cas de défaillance
- Meilleure sécurité des données : pas de sauvegardes automatiques
- Meilleur monitoring : impossible de suivre les performances du système
- Et plus encore !

---

<div align="center">
  <sub>Créé avec ❤️ par AI Swiss</sub>
</div>
