# Exemple de projet : rédiger un rapport complexe

Dans ce tutoriel, on va voir comment co-créer avec l'IA un rapport complexe intitulé "IA : notre ambition pour la Suisse". Avec notre nouvel ami Cursor, bien sûr.

## Approche structurée en 4 étapes

### 1. Créer un premier jet de document d'instructions

Créez un fichier `instructions_v1.0.0.md` avec en suivant par exemple ce format :
````markdown
# Instructions

## But
(Les grandes lignes de ce qu'on veut accomplir)

## Besoins
(Les exigences du projet)

## Spécifications
(Quelques détails sur la manière dont les besoins doivent être satisfaits)

## Documentation
(Quelques sources utiles à la réalisation du projet)

## Tâches
(Une ébauche d'étapes de réalisation du projet, si possible. Idéalement des tâches simples et bien définies.)
````

L'IA peut bien sûr vous aider à remplir ce template.

### 2. Peaufiner les instructions avec l'IA

Sur la base du premier jet, utilisez l'IA pour créer une nouvelle version `instructions_v1.0.0.md` plus précise pour un spécialiste qui devrait être en mesure de réaliser les tâches.

Dans Composer, demandez par exemple :
```
Crée un fichier d'instructions `instructions_v1.1.0.md` détaillant @instructions_v1.0.0.md pour que tout soit clair et précis pour un expert d'une commission scientifique qui doit réaliser le projet.

- Inclus toutes mes instructions.
- Ne crée pas de rapport, juste des instructions.
```

Relisez la version `instructions_v1.1.0.md` et ajustez au besoin avec l'aide de l'IA.

### 3. Générer le rapport

C'est là que la magie va se faire ! Ouvrez Composer (`Ctrl/⌘ + I`) et exécutez les tâches une par une :

```
Lis attentivement mes instructions dans @instructions_v1.1.0.md et exécute la tâche 1
```

Pour chaque tâche :
1. Vérifiez le résultat généré
2. Ajustez si nécessaire avec l'aide de l'IA
3. Passez à la tâche suivante une fois satisfait

Une fois toutes les tâches exécutées, cliquez sur "Apply all" pour valider tous les fichiers générés.

### 4. Agréger le contenu

Pour finir, on peut agréger les fichiers correspondant aux différentes sections du rapport dans un seul fichier `rapport_final.md`. Pour ça, demandons à l'IA de nous aider avec un script Python :

Prompt :
```
Crée un script Python `script.py` dans le répertoire `rapport_final` pour agréger les fichiers "6_section_<nombre>_<titre>.md" du répertoire `contenu_généré` en un fichier `rapport.md` dans `rapport_final`. @

- Les fichiers doivent être agrégés dans l'ordre de leur nom ("6_section_<nombre>_<titre>.md"), bout à bout avec juste une ligne vide entre deux, et sans commentaires additionnels.
- Donne la marche à suivre pour exécuter le script, sachant que j'ai déjà installé Python.
```

L'IA devrait créer le script et vous fournir les instructions pour le lancer.

A vous de jouer ! L'IA est là pour vous aider à chaque étape. Et au pire, les humains d'AI Swiss sont toujours là pour vous aider.
