<div align="center">
  <h1>🏭 Bibliothèque de Workflows IA</h1>
  <p><i>Transformez des tâches IA complexes en étapes simples et répétables</i></p>
</div>

## À quoi sert cette bibliothèque ?

Vous avez déjà souhaité :
- Sauvegarder vos meilleures conversations IA pour les réutiliser ?
- Partager votre expertise IA avec votre équipe ?
- Obtenir des résultats cohérents de l'IA ?
- Construire sur ce qui fonctionne plutôt que repartir de zéro ?

C'est exactement ce que cette bibliothèque vous permet de faire ! Considérez-la comme votre collection de recettes IA qui :
- Fonctionnent de manière fiable à chaque fois
- S'améliorent à chaque utilisation
- Sont accessibles à tous
- Se déploient à l'échelle des équipes

## Pour commencer

### 1. Utiliser un workflow existant
C'est aussi simple que :
1. Ouvrir Cursor AI Composer (CMD/CTRL + I)
2. Copier le contenu d'un fichier `run.md`
3. Remplir vos détails spécifiques
4. Appuyer sur Entrée et regarder la magie opérer !

### 2. Créer votre propre workflow
La façon la plus simple :
1. Aller dans `factory/new_workflow/`
2. Suivre les étapes dans `run.md`
3. Obtenir un workflow professionnel en quelques secondes

## Organisation de la bibliothèque

```
_ai_workflows/
├── code_based/            # Workflows avec automatisation Python
│   └── faq_analysis/      # Exemple : amélioration de FAQ
├── factory/               # Création de nouveaux workflows
│   ├── new_workflow/      # Template de workflow complet
│   └── new_instructions/  # Template de tâche unique
├── templates/             # Modèles réutilisables
└── text_based/           # Workflows textuels
```

## Deux façons d'utiliser les workflows

### 1. Workflows textuels
Parfaits quand vous voulez :
- Expérimenter rapidement
- Discuter des idées avec l'IA
- Affiner les choses de manière interactive
- Garder les choses simples

### 2. Workflows en code
Meilleurs quand vous devez :
- Exécuter les choses automatiquement
- Avoir plus de contrôle
- Intégrer avec d'autres outils
- Être indépendant des assistants IA

## Types de workflows

### Workflows complets
Pour les processus à répéter :
```
workflow_name/
├── instructions/    # Guide étape par étape
│   └── instructions_v1.0.0.md
└── run.md          # Prêt à exécuter
```

### Instructions simples
Pour les tâches complexes uniques :
```
project_name/
└── instructions_v1.0.0.md
```

## Bonnes pratiques

### Suivi des modifications
- Utilisez des numéros de version (v1.0.0)
- Documentez les changements
- Gardez les versions précédentes

### Assurance qualité
- Les fichiers commencent par `__validation_required`
- Vérifiez toujours les résultats
- Retirez le suffixe après validation
- Testez avec différentes entrées

### Principes de conception
- Un objectif clair par workflow
- Entrées et sorties standardisées
- Critères de succès clairs
- Améliorations régulières

## Essayez un exemple

Découvrez le workflow d'analyse de FAQ dans `code_based/faq_analysis/` :
- Version texte pour les expérimentations rapides
- Version code pour l'automatisation
- Documentation complète
- Prêt à l'emploi !

## En savoir plus

- Commencez par créer votre propre workflow avec notre [factory](factory/new_workflow/run.md)
- Consultez les [tutoriels](_ai_workflows_tutorials/README.md)

## Envie de contribuer ?

1. Essayez les workflows existants
2. Testez dans vos projets
3. Documentez ce que vous apprenez
4. Partagez vos améliorations

---

<div align="center">
  <sub>Créé avec ❤️ par AI Swiss</sub>
</div>
