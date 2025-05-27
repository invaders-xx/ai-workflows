<div align="center">
  <h1>🤖 Framework AI Workflows</h1>
  <p><i>Transformez vos conversations avec les assistants IA en code Python puissant</i></p>
</div>

## Pourquoi ce framework ?

Vous aimez travailler avec les assistants IA - écrire des instructions en texte simple, avoir des conversations naturelles, obtenir des résultats rapidement. Mais parfois vous avez besoin de plus :

- Vous voulez exécuter le même workflow de manière fiable, encore et encore ?
- Vous devez d'abord traiter des données provenant de plusieurs sources ?
- Vous voulez un contrôle précis sur le raisonnement de l'IA ?
- Vous devez intégrer vos outils existants ?

C'est là que ce framework intervient. Il vous aide à transformer vos workflows IA textuels en code Python qui :
- S'exécute indépendamment de tout assistant IA
- Utilise des bibliothèques open-source éprouvées
- Vous donne un contrôle total sur l'exécution
- S'adapte à vos besoins

## Prérequis

1. **Environnement Python**
   - Python 3.10 ou supérieur
   - Poetry (gestionnaire de paquets)

2. **Accès API aux modèles IA**
   - Vous pouvez par exemple créer un compte gratuit sur [Groq](https://console.groq.com) et générer une clé API

## Exemple rapide

Consultez l'[exemple d'analyse de FAQ](_ai_workflows/code_based/faq_analysis) pour un exemple complet et fonctionnel.

## Installation

1. **Récupérer le code**
   - Cloner le dépôt : `git clone https://github.com/cbardyn/ai-swiss-workflows`
   - Naviguer vers le package : `cd _ai_workflows_packages/ai_workflows`

2. **Installer les dépendances**
   - Installer avec Poetry : `poetry install`
   - Activer l'environnement :
     - Linux/macOS : `source .venv/bin/activate`
     - Windows : `.\.venv\Scripts\activate`

3. **Vérifier l'installation**
   - Essayer un exemple : `cd ../../_ai_workflows/code_based/faq_analysis/_code && python run.py`

## Guide d'utilisation pas à pas

### 1. Créer la structure de votre projet
Créez trois fichiers principaux dans votre répertoire de projet :
- config.yaml (configuration IA)
- instructions.yaml (vos tâches de workflow)
- run.py (exécuteur Python)

### 2. Écrire votre fichier d'instructions
Dans instructions.yaml, définissez :
- Votre objectif de workflow
- Les tâches à effectuer
- Les fichiers d'entrée à analyser
- Les fichiers de sortie à générer

Astuce : Commencez par un workflow textuel dans instructions_v1.0.0.md et utilisez votre assistant IA pour le convertir en format YAML.

### 3. Configurer les outils IA
Dans config.yaml, spécifiez :
- Votre choix de modèle IA (par ex., LLaMA de Groq)
- Votre clé API
- Les paramètres du modèle (température, etc.)

### 4. Créer votre exécuteur
Dans run.py, utilisez le framework pour :
- Configurer la journalisation
- Charger votre configuration
- Exécuter votre workflow

### 5. Exécuter votre workflow
Simplement exécuter : `python run.py`

## Obtenir de l'aide

1. Consultez l'[exemple d'analyse de FAQ](_ai_workflows/code_based/faq_analysis) pour un exemple complet
2. Parcourez le [tutoriel](_ai_workflows_tutorials/3_ai_workflows_as_code/) des workflows basés sur le code

## Fonctionnalités du framework

### Gestion intelligente du contexte
Le framework automatiquement :
- Charge les fichiers et URLs
- Crée des bases de données vectorielles consultables
- Trouve les informations pertinentes pour chaque tâche

### Orchestration des tâches
Le framework gère :
- Le séquencement des tâches
- Le passage d'informations entre les tâches
- Le suivi de la progression

### Gestion des erreurs
Gestion intégrée pour :
- Fichiers manquants
- Échecs d'API
- Configurations invalides

## Améliorations possibles

- Plus de connecteurs vers des systèmes externes (Dropbox, Google Drive, etc.)
- Meilleurs tests : Pas encore de tests automatisés pour garantir un fonctionnement parfait
- Meilleure sécurité : Les clés API sont stockées dans des fichiers texte simples
- Meilleures performances : Les tâches s'exécutent les unes après les autres au lieu d'en parallèle
- Meilleure fiabilité : Pas de modèles IA de secours si le principal échoue
- Meilleure sécurité des données : Pas de sauvegardes automatiques de vos données
- Meilleur monitoring : Impossible de suivre les performances du système
- Et plus encore !

---

<div align="center">
  <sub>Construit avec ❤️ par AI Swiss</sub>
</div>
