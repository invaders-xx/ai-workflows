# Bienvenue dans l'univers de Cursor !

## Tout d'abord : pourquoi un tutoriel au format ".md" ?

Le fichier que vous lisez actuellement est en "Markdown" (.md). C'est un format de texte qui permet de décrire le formattage directement dans le texte, plutôt qu'en cliquant sur des boutons et menus. Au lieu de sélectionner du texte et de cliquer sur "Italique" comme dans Word, on ajoute par exemple deux étoiles autour du texte. Simple et efficace !

L'avantage ? Déjà, la mise en forme fonctionne partout. C'est pour ça que le Markdown est très populaire, de la gestion de notes personnelles à la rédaction de documentation technique.

L'avantage ici ? C'est le format idéal pour écrire des instructions pour l'IA.

### Les essentiels du Markdown

#### Les titres

Pour créer un titre, utilisez le symbole `#`. Plus vous mettez de `#`, plus le titre sera petit :
# Grand titre
## Moyen titre
### Petit titre
#### Etc.

#### Le texte stylé

- *Pour l'italique*, encadrez avec des *étoiles*
- **Pour le gras**, utilisez **deux étoiles**
- Pour combiner les deux : ***texte en gras italique***

#### Les listes

Pour une liste simple :
- Un élément
- Un autre
  - Un sous-élément (avec 2 espaces avant le tiret)
  - Encore un

Pour une liste numérotée :
1. Première chose
2. Deuxième chose
   1. Sous-point
   2. Autre sous-point

#### Les liens

Pour créer un lien, c'est comme une mini-équation :
[Ce que les gens voient](l'adresse-du-lien)

Par exemple : [Le site AI Swiss](https://www.a-i.swiss)

### Pour aller plus loin

- [Guide Markdown en français](https://joplinapp.org/fr/help/apps/markdown/)
- [Éditeur Markdown en ligne](https://dillinger.io/) pour s'entraîner

Le meilleur moyen d'apprendre ? Expérimentez directement dans ce fichier ! Modifiez le texte et observez le résultat.

## Entrons dans le vif du sujet : pourquoi Cursor ?

Maintenant que vous maîtrisez les bases du Markdown, découvrons l'outil qui va transformer votre façon de travailler :

[Cursor AI (ou Cursor)](https://cursor.com) est un éditeur de fichiers intelligent permettant de révolutionner votre façon de travailler avec l'IA. Il est basé sur [VS Code](https://code.visualstudio.com/), un éditeur de code de Microsoft très populaire.

Cursor évolue en parallèle de VS Code, bénéficiant de toutes ses fonctionnalités tout en l'enrichissant avec des fonctionnalités d'IA toujours plus puissantes.

Cursor est souvent perçu comme un outil réservé aux développeurs, mais on va vous prouver que c'est faux : si un outil est capable de gérer des milliers de fichiers de code interconnectés, de maintenir du contexte à travers des langages de programmation différents, et d'orchestrer des modifications cohérentes à grande échelle... ne serait-il pas parfait pour d'autres types de projets complexes ?

Chez AI Swiss, nous sommes convaincus que Cursor est actuellement (en date du 2024-11-12) l'éditeur le plus puissant pour travailler avec l'IA, et nous allons vous montrer pourquoi.

**Attention** :

Cursor est **actuellement** (en date du 2024-11-12) l'outil le plus puissant pour travailler avec l'IA, mais le domaine évolue rapidement : [GitHub Copilot](https://github.com/features/copilot), lui aussi basé sur VS Code, offre une expérience qui s'approche de celle de Cursor et pourrait devenir un jour supérieure.

Rassurez-vous, les méthodes que nous allons explorer sont transposables sur n'importe quel outil.

### Les points forts de Cursor

1. **Tout au même endroit**
   Fini le jonglage entre applications. Vous pouvez créer, organiser et modifier vos fichiers avec l'IA au même endroit.

2. **Du contexte à gogo**
   Contrairement à ChatGPT et ses semblables, Cursor peut prendre en compte tous les fichiers de votre projet. Cela permet des interactions beaucoup plus pertinentes.

3. **Une interface et des raccourcis efficaces**
   C'est l'avantage d'un outil conçu pour les codeurs : il y a des raccourcis pour tout.
   - `Ctrl/⌘ + L` pour ouvrir une conversation avec l'IA
   - `Ctrl/⌘ + K` pour demander de l'aide à l'IA à n'importe quel endroit précis
   - `Ctrl/⌘ + I` pour faire de l'édition intelligente multi-fichiers avec "Composer", relâchant toute la puissance de Cursor comme on le verra plus tard
   - Etc.

Prêt à explorer ce monde magique mais réel ? C'est parti !

### Installation (probablement déjà faite)

1. Téléchargez Cursor sur [cursor.com](https://cursor.com)
2. Installez-le comme n'importe quelle application

Pour les utilisateurs de VS Code : vous pouvez importer vos paramètres existants au premier lancement.

### Cursor AI, GitHub Copilot... : des outils puissants, oui, mais jamais gratuits

Les modèles d'IA puissants comme Claude 3.5 Sonnet ou GPT-4o sont devenus de l'infrastructure de base pour les outils d'IA. Et toute infrastructure a un coût. Trois options s'offrent à vous (par ordre de recommandation) :

1. **Cursor Pro**
   - USD 192.00 par an (soit USD 16.00 par mois)
   - Accès aux principaux modèles dernier cri (Claude 3.5 Sonnet, GPT-4o, etc.)

2. **GitHub Copilot**
   - USD 100.00 par an (soit USD 8.33 par mois)
   - Accès aux principaux modèles dernier cri (Claude 3.5 Sonnet, GPT-4o, etc.)
   - Aussi basé sur VS Code, mais pour l'instant avec des fonctionnalités d'IA plus limitées (même dans le nouveau Copilot Spark).

On peut aussi utiliser Cursor en donnant accès à des modèles via des clés API, et donc de payer l'accès à un modèle à d'autres fournisseurs comme OpenAI. Le désavantage est que les coûts sont souvent au final plus élevés et que les modèles de Cursor permettant l'autocomplétion intelligente notamment ne seront pas disponibles. Voir [ici](https://docs.cursor.com/advanced/api-keys) pour les détails.

### Confidentialité et sécurité

Cursor et ses semblables (GitHub Copilot, notamment) prennent la protection des données très au sérieux puisqu'ils sont utilisés pour du code dans de grosses entreprises.

En activant le "Privacy Mode" dans les paramètres de Cursor (important !), on garantit en principe que :
  - Aucune donnée n'est stockée
  - Aucune donnée n'est utilisée pour l'entraînement de modèles
  - Aucune donnée n'est partagée avec des tiers

Les détails :
- [Politique de sécurité](https://www.cursor.com/security)
- [Politique de confidentialité](https://www.cursor.com/privacy)

## Passons à la partie plus fun : les fonctionnalités magiques de Cursor !

### L'incontournable chat IA

Le chat est devenu l'interface de base pour interagir avec l'IA. Pour l'utiliser sur Cursor :

1. Ouvrez le chat avec `Ctrl/⌘ + Alt/Option + L` (L comme "Lumière suprême du savoir")
2. Sélectionnez un modèle d'IA (chez AI Swiss, on a un faible pour `claude-3-5-sonnet`, en date du 2024-11-12)
3. Posez une question (faites un "prompt")
4. Validez avec `Enter` ou cliquez sur `Chat`

Plusieurs options sont disponibles pour chaque message :
- `Edit` pour peaufiner votre prompt
- `Reply` au-dessus de chaque réponse de l'IA pour y répondre spécifiquement
- `Copy message` pour copier un message dans le presse-papiers

#### Exemple pratique

1. Ouvrez le chat (`Ctrl/⌘ + Alt/Option + L`)
2. Sélectionnez `claude-3-5-sonnet`
3. Écrivez un prompt comme :
   "Quel est le sens de la vie, l'Univers et le reste ?"
4. Observez la réponse.

Vous remarquerez ici que les réponses sont encadrées par "---". C'est dû à notre fichier `.cursorrules` qui définit un style de réponse. Nous verrons ça plus tard.

#### Historique des conversations

Cursor propose deux méthodes pour accéder à un historique :

1. **Depuis le chat**
   - En cliquant sur `Previous Chats` en haut à droite (`Ctrl/⌘ + Alt/Option + L`)

2. **Depuis votre explorateur de fichiers**
   - Les conversations sont sauvegardées dans les données de l'application Cursor. Mais bonne chance pour les trouver et surtout les utiliser !

On vous conseille plutôt des options de sauvegarde **locale** :

1. **Sauvegarde automatique**
   - Utilisez [cursor-chat-export](https://github.com/somogyijanos/cursor-chat-export) pour exporter l'historique complet vers un fichier `.history` dans votre projet

2. **Sauvegarde manuelle sélective**
   - Créez un fichier `.history.md` dans votre projet
   - Copiez-y les conversations les plus importantes au fur et à mesure de votre projet

Avantages de la sauvegarde locale :
- **Facile à parcourir** : retrouvez rapidement vos conversations
- **Toujours disponible** : même si vous changez d'ordinateur
- **Versionnée avec votre projet** : pour ceux qui utilisent Git par exemple

### L'ajout de contexte : la clé pour interagir efficacement avec l'IA

Comme le chat, l'ajout de contexte est un incontournable des outils d'IA. Sur Cursor, on peut facilement ajouter :

#### 1. Des fichiers locaux
- Cliquez sur `+ Add context` en haut à gauche
- Ou mentionnez un fichier directement dans votre message :
  - Option 1 : Cliquez sur `@ Mention` ou `Image`
  - Option 2 : Tapez `@Files` et sélectionnez un fichier
  - Option 3 : Glissez-déposez un fichier

Exemple de prompt :
```
Ce rapport contient-il des éléments sur la Suisse ? @rapport_de_la_commission_de_l'ia_en_france.md
```

Note : Cursor ne digère pas encore les PDF. Pour les utiliser, copiez leur contenu dans un fichier texte (.md par exemple).

#### 2. Des pages web individuelles
Tapez `@` suivi de l'URL :
```
Quel est le prochain événement de AI Swiss? @https://www.a-i.swiss
```

Note : Cursor ne va pas explorer plus loin que la page mentionnée, donc choisissez bien ! C'est pareil sur ChatGPT.

#### 3. Des sites web
1. Tapez `@Docs`
2. Cliquez sur `+ Add new doc`
3. Entrez l'URL et un nom simple (exemple : `https://www.a-i.swiss` → `AI Swiss`)

```
Quel est le prochain événement de AI Swiss? @AI Swiss
```

Notes :
- Le contexte @Docs reste actif pour toute la conversation jusqu'à sa suppression manuelle.
- Il est souvent préférable d'utiliser `@Web` (décrit ci-dessous) pour permettre à l'IA de chercher des pages seule sur internet.

#### 4. Des recherches web en direct
Ajoutez `@Web` à votre prompt pour permettre à l'IA de faire ses propres recherches (pour obtenir des informations à jour, vérifier des faits, etc.) :
```
Quels sont les 10 articles les plus récents concernant l'IA sur https://www.nature.com? Collecte les articles avec titre, lien, date et bref résumé de leur importance. Donne-moi ensuite la liste par ordre chronologique. @Web
```

#### 5. Un projet entier
Pour inclure tout votre projet :
- Option 1 : Tapez `@Codebase` dans votre prompt
- Option 2 : Utilisez `Ctrl/⌘ + Enter` pour envoyer votre prompt (au lieu de cliquer sur `chat` ou d'appuyer sur `Enter`)

L'avantage de `@Codebase` est qu'il permet de spécifier des paramètres de recherche (fichiers à inclure, exclure, étape de raisonnement, etc.) directement dans la fenêtre de prompt.

Exemple :
```
Est-ce que je parle de ce que la mention "Codebase" fait sur Cursor dans mon projet? @Codebase
```

Astuce : Créez un fichier `.cursorignore` à la racine du projet pour exclure systématiquement des fichiers non pertinents des recherches `@Codebase`.

## L'édition intelligente avec Cursor : les petits plus qui font toute la différence

### Autocomplétion prédictive

Cursor propose des suggestions à mesure que vous écrivez :
- Commencez à écrire
- Observez les suggestions apparaître en gris
- Acceptez avec `Tab` ou continuez à taper

Testez par vous-même :
Écrivez "Cursor est un..." et laissez la magie opérer.

### Navigation intelligente

Cursor prédit où vous allez probablement faire vos prochains changements :
- Quand un indicateur au contour orange `tab` apparaît, appuyez sur `Tab` pour sauter directement à l'endroit prédit

Exemple très simple :
Transformer cette liste en liste à puces :
```
Titre
Introduction
Méthode
Discussion
Conclusion
```

1. Ajoutez un tiret (`-`) au premier élément
2. Observez la suggestion d'ajouter un tiret à d'autres éléments
3. Utilisez `Tab` pour accepter
4. Cursor vous suggère un saut avec Cursor Tab, acceptez avec `Tab`
5. Continuez avec `Tab` pour les éléments suivants

### Édition assistée locale

Pour des modifications ciblées, utilisez `Ctrl/⌘ + K` à n'importe quel endroit du texte. Cursor peut :
- Corriger l'orthographe et la grammaire
- Traduire
- Reformuler pour plus de clarté
- Adapter le style selon vos besoins
- Optimiser la structure du texte
- Etc.

Exemples de demandes :
```
- "Orthographe ?"
- "Améliore"
- "Ajoute des exemples"
- "Reformule pour un non-codeur"
- Etc.
```

## Et enfin : Composer, l'éditeur de fichiers multiples qui change tout

Vous maîtrisez maintenant les bases de Cursor. Il est temps de découvrir sa fonctionnalité la plus puissante : Composer, un outil qui permet de créer et de modifier un ensemble de fichiers simultanément !

Pour l'utiliser :
1. Ouvrez Composer avec `Ctrl/⌘ + I` (I comme "I want this")
2. Décrivez ce que vous souhaitez créer
3. Affinez les résultats selon vos besoins

### Exemple pratique

```
Crée un kit de démarrage pour mon club de lecture sur l'IA comprenant :
- Un calendrier des rencontres 2025 (calendrier_2025.md)
- Une fiche de lecture type (fiche_lecture_type.md)
- Un tableau de suivi des lectures passées (bibliotheque.csv)
- Un guide d'animation de discussion (guide_animation.md)
- Un modèle de newsletter mensuelle (newsletter_type.md)
- Des suggestions de questions pour les débats (questions_types.md)
Recherche @Web des lectures incontournables récentes
```

Composer générera tous ces fichiers en une seule opération, avec la possibilité d'affiner chaque fichier selon vos besoins. Nous verrons plus tard comment l'utiliser dans un cas concret.

Pour apprécier pleinement la puissance de Composer, essayez de réaliser la même tâche avec d'autres outils comme ChatGPT ou Claude. Vous verrez à quel point Cursor se distingue !

## Quelques astuces pour tirer le meilleur de Cursor

Pour terminer, voici quelques configurations et astuces qui rendront votre expérience encore plus productive :

### Personnalisation avec .cursorrules

Créer un fichier `.cursorrules` pour personnaliser le comportement global de l'IA selon vos besoins :

1. Créez un fichier `.cursorrules` **à la racine de votre projet**
2. Ajoutez un prompt de personnalisation
3. Testez dans un nouveau chat

#### Exemple simple
```
Réponds toujours en commençant par "Je réponds, mais seulement parce que c'est toi."
```

Pour des exemples plus utiles, consultez le dossier [exemples_de_fichiers_cursorrules](./exemples_de_fichiers_cursorrules). Le fichier `.cursorrules_pour_apprendre` notamment permet de faire de Cursor un instructeur de programmation et d'IA qui vous guide à chaque interaction.

### Mode "Long Context"

Le mode "Long Context" permet de prendre en compte plus d'éléments du contexte spécifié. Pour l'activer :

#### Activation
1. Allez dans les paramètres de Cursor sous l'onglet "Beta" 
2. Activez "Long Context Chat"

#### Utilisation
1. Nouveau chat (`Ctrl/⌘ + L`)
2. Sélectionnez "Long Context Chat" au lieu de "Normal Chat" en haut à droite
3. Choisissez `claude-3-5-sonnet-200k` (notre recommandation en date du 2024-11-12)

Pour en savoir plus : [Documentation officielle](https://docs.cursor.com/advanced/models#long-context-only-models)

Et voilà ! Si vous êtes arrivé là, vous savez tout !