<div align="center">
  <h1>🤖 Framework AI Workflows</h1>
  <p><i>Des conversations avec l'assistant IA au code autonome</i></p>
</div>

## Pourquoi ce framework ?

Imaginez que vous écrivez des instructions pour un assistant IA comme Cursor AI. C'est intuitif - vous écrivez ce que vous voulez en texte simple, discutez des détails avec l'IA et obtenez des résultats. Mais parfois vous avez besoin de plus :
- Et si vous devez traiter des données de sources externes d'abord ?
- Et si vous voulez exécuter le même workflow automatiquement, sans ouvrir d'assistant IA ?
- Et si vous voulez plus de contrôle sur la façon dont l'IA traite vos instructions ?

C'est là que ce framework intervient. Il vous aide à transformer vos workflows textuels en code Python qui :
- S'exécute indépendamment de tout assistant IA
- Utilise des bibliothèques open-source que vous contrôlez
- Vous donne plus de pouvoir sur l'exécution

## Comprendre les deux approches

### Workflows textuels : puissants mais parfois limités
```
Vous → Écrivez des instructions en texte → Discutez avec l'assistant IA → Obtenez des résultats
```

**Parfait quand vous avez besoin :**
- d'expérimentation rapide
- d'échanges naturels avec l'IA
- de modifications faciles à la volée
- de ne pas coder

**Moins adapté quand vous avez besoin :**
- de traiter des données externes d'abord
- d'exécuter les choses automatiquement
- d'intégrer avec d'autres systèmes
- d'un contrôle précis sur l'exécution

### Workflows en code : plus puissants mais moins interactifs
```
Vous → Écrivez du YAML structuré → Exécutez du code Python → Obtenez des résultats
```

**Parfait quand vous avez besoin :**
- d'indépendance vis-à-vis des assistants IA
- d'exécution automatique
- d'intégration avec d'autres outils
- de plus de contrôle sur le processus

**Moins adapté quand vous avez besoin :**
- de changements rapides à la volée
- de discuter des cas particuliers avec l'IA
- d'explorer des solutions créatives
- d'éviter d'écrire du code

## Comment ce framework aide

Nous avons créé des outils (dans `_ai_workflows_packages/ai_workflows/`) qui vous aident à :

1. **Garder des instructions simples**
   ```yaml
   # instructions.yaml - Toujours lisible comme du texte !
   goal: |
     Analyser une FAQ et suggérer des améliorations
   tasks:
     - Extraire les Q&R du site web
     - Analyser les manques
     - Générer des suggestions de réponses
   ```

2. **Choisir vos outils IA**
   ```yaml
   # config.yaml - Choisissez les modèles IA que vous voulez
   llm:
     type: "langchain_groq.ChatGroq"
     model_name: "llama-3.3-70b-versatile"
   ```

3. **Exécuter n'importe où**
   ```python
   # Code Python simple pour exécuter votre workflow
   from ai_workflows import Workflow
   
   workflow = Workflow('config.yaml', 'instructions.yaml')
   result = workflow.run()
   ```

## Voir en action : analyseur de FAQ

Regardons un exemple concret qui :
- Lit des FAQs depuis des sites web
- Trouve les manques
- Suggère de nouvelles réponses

### 1. D'abord, essayez-le en version texte
Dans `_ai_workflows/code_based/faq_analysis/_text/` :

1. **Écrivez des instructions simples**
   ```markdown
   # Instructions
   1. Extraire la FAQ du site web
   2. Analyser les nouvelles questions
   3. Suggérer des réponses
   4. Créer un rapport
   ```

2. **Exécutez dans votre assistant IA**
   - Copiez le contenu de `run.md`
   - Discutez des résultats avec l'IA
   - Affinez si nécessaire

### 2. Puis, essayez-le en code
Dans `_ai_workflows/code_based/faq_analysis/_code/` :

1. **Mêmes instructions, plus structurées**
   ```yaml
   tasks:
     - key: 'extract_faq'
       description: 'Obtenir les Q&R du site'
     - key: 'analyze_questions'
       description: 'Trouver les manques'
   ```

2. **Exécutez n'importe où**
   ```bash
   python run.py
   ```

Les deux créent les mêmes sorties dans `_output/` :
- FAQ extraite du site web
- Analyse des sujets manquants
- Suggestions de nouvelles réponses
- Rapport complet

Mais la version code :
- S'exécute sans assistant IA
- Donne plus de contrôle
- S'intègre mieux avec d'autres outils
- Gère mieux les erreurs

## Essayez par vous-même

1. **Installation (une seule fois)**
   ```bash
   # Récupérez le code
   git clone https://github.com/cbardyn/ai-swiss-workflows
   cd _ai_workflows_packages/ai_workflows
   
   # Installez les dépendances
   poetry install
   source .venv/bin/activate  # (ou .\.venv\Scripts\activate sous Windows)
   ```

2. **Exécutez l'exemple**
   ```bash
   cd ../../_ai_workflows/code_based/faq_analysis/_code
   python run.py
   ```

3. **Créez le vôtre**
   - Commencez par des instructions textuelles
   - Convertissez en YAML quand vous êtes prêt
   - Configurez vos outils IA
   - Exécutez indépendamment

## Quand utiliser quoi

### Restez en texte quand :
- Vous explorez de nouvelles idées
- Vous avez besoin de l'input créatif de l'IA
- Vous voulez des itérations rapides
- Vous n'avez pas besoin d'automatisation

### Passez au code quand :
- Vous avez besoin d'automatisation
- Vous voulez plus de contrôle
- Vous devez intégrer avec d'autres outils
- Vous voulez l'indépendance des assistants IA

## En savoir plus
- Détails du framework : `_ai_workflows_packages/ai_workflows/README.md`
- Exemples : `_ai_workflows/code_based/*/README.md`

---

<div align="center">
  <sub>Créé avec ❤️ par AI Swiss</sub>
</div>
