# Co-réaliser un projet complexe avec l'IA

Vous essayez de réaliser un projet ambitieux sur ChatGPT et vous vous perdez rapidement dans vos prompts sans trop savoir ce qu'il a gardé en mémoire ? Voici une méthode simple éprouvée pour utiliser l'IA beaucoup plus efficacement :

## L'essentiel : des instructions claires

Les LLMs actuels ne sont pas tout puissants. Ils ne sont pour l'instant capables de réaliser un projet complexe que si on le décompose en étapes simples. Et comme à un nouveau collègue, il faut leur donner des instructions claires sur notre façon de travailler. Même ChatGPT-100o ne saura pas lire dans vos pensées (on espère !).

## La clé pour ne pas se perdre : des fichiers d'instructions

Que ce soit pour rédiger un roman, un acte légal ou un rapport scientifique, il faut absolument faire évoluer un ou plusieurs fichiers d'instructions au fur et à mesure des interactions avec l'IA.

Des fichiers d'instructions bien pensés permettent de :

1. Clarifier le projet pour vous (un peu comme définir les besoins d'un projet traditionnel)
2. Clarifier le projet pour l'IA
3. Itérer en cycle court avec l'IA pour clarifier tout ça au fur et à mesure
4. Garder une trace du processus (en versionnant par exemple les fichiers d'instructions)
5. Permettre à n'importe qui (et à vous dans 6 mois) de reprendre le projet, en partant des fichiers d'instructions existants

## Concrètement : une approche en trois temps

### 1. Écrire un premier jet d'instructions

Créez un fichier nommé par exemple `instructions_v1.0.0.md` et décrivez ce que vous souhaitez réaliser sans trop vous préoccuper des détails. Le but de travailler avec l'IA est aussi de minimiser la charge mentale !

Chattez avec l'IA pour jeter les bases. Ne vous inquiétez pas si tout n'est pas parfait; ce n'est que le point de départ d'un processus itératif.

On vous propose le template `instructions_v1.0.0.md` ci-joint, qui se présente ainsi :

```markdown
# Instructions

## But
Décrivez votre objectif en quelques phrases simples.

## Besoins
Listez ce qui est nécessaire pour atteindre votre but.

## Spécifications
Ajoutez des détails techniques, des contraintes importantes, etc.

## Documentation
Rassemblez des ressources utiles : liens, références, exemples, etc.

## Tâches
Esquissez les grandes étapes de la réalisation du projet, même approximativement.
```

### 2. Affiner constamment avec l'IA

Une fois la base posée, continuez à itérer avec l'IA. Soit sur le fichier d'instructions `v1.0.0`, soit sur une nouvelle version `v1.1.0` en demandant par exemple à Composer :

```
Crée un fichier d'instructions `instructions_v1.1.0.md` détaillant @instructions_v1.0.0.md pour que tout soit clair et précis pour un expert qui doit réaliser le projet.

- Inclus toutes les instructions existantes
- Ajoute les détails manquants, clarifie les instructions floues
- Ne crée pas de code, juste des instructions

Et surtout, décompose la réalisation de ce projet en une liste d'étapes claires et bien définies, spécifiant les fichiers à produire.
```

Examinez le résultat et itérez avec l'IA en demandant par exemple :
- "Donne-moi dix autres façons de réaliser ce projet pour mieux comprendre si je fais fausse route."
- "Ajoute ce nouveau besoin client : (...)"
- "Ajoute une étape pour créer ce document pour mon quality manager : (...)"
- etc.

### 3. Passez à la réalisation sur Composer

Une fois vos instructions jugées claires, tournez-vous vers votre meilleur ami : Composer (`Ctrl/⌘ + I`)

1. **Demandez-lui d'exécuter la première tâche** :
```
Lis attentivement mes instructions dans @instructions_v1.1.0.md et exécute la tâche 1
```

2. **Vérifiez et ajustez** ce qu'il a généré

3. **Continuez tâche par tâche** :
```
Exécute la tâche 2
```

puis 3, 4, etc.

## Quelques astuces pour une co-réalisation réussie

### Utiliser le panneau de contrôle
- Ouvrez-le avec `Ctrl/⌘ + Shift + I`
- Gardez un œil sur les fichiers générés

### Rebrousser chemin quand vous sentez que vous faites fausse route
- Utilisez les checkpoints pour revenir en arrière
- Créez de nouvelles versions de vos fichiers d'instructions (v1.0.0, v1.1.0, etc.) au fur et à mesure pour garder une trace

## Itérer, itérer, ...

...itérez.

## Exemples de projets complexes qui deviennent soudainement accessibles

## Pour tout un chacun
- Organiser un événement (mariage, anniversaire, conférence)
- Planifier un voyage complexe
- Créer un budget familial
- Rédiger un CV et lettres de motivation personnalisés
- Organiser une bibliothèque numérique personnelle
- Mettre en place un système d'archivage familial
- Etc.

## Pour les créatifs
- Écrire un livre ou un scénario
- Créer un blog ou une newsletter
- Développer une stratégie de contenu social media
- Concevoir un portfolio en ligne
- Créer un cours en ligne
- Monter un podcast
- Etc.

## Pour les entrepreneurs
- Rédiger un business plan
- Créer un pitch deck
- Mettre en place un système CRM simple
- Développer un kit de communication
- Organiser un lancement de produit
- Créer des processus d'entreprise
- Etc.

## Pour tout professionnel
- Rédiger des rapports complexes
- Créer des présentations impactantes
- Organiser une base de connaissances
- Mettre en place un système de veille
- Développer des workflows d'équipe
- Créer des templates de documents
- Gérer un projet de recherche
- Etc.

## Pour les éducateurs
- Créer un programme de cours
- Développer du matériel pédagogique
- Organiser des évaluations
- Mettre en place un suivi des élèves
- Créer des exercices personnalisés
- Développer des projets éducatifs
- Etc.

## Pour les techniciens
- Créer des sites web
- Développer des applications
- Mettre en place des outils de productivité
- Documenter des systèmes techniques
- Créer des scripts d'automatisation
- Développer des prototypes
- Etc.

## Pour les chercheurs
- Organiser une revue de littérature
- Structurer une thèse ou un article
- Analyser des sources complexes
- Préparer une demande de subvention
- Développer un protocole de recherche
- Gérer un projet de recherche collaboratif
- Etc.

Et plus encore !

L'important est de commencer avec un objectif clair, de décomposer le projet en étapes simples pour l'IA et d'itérer progressivement.