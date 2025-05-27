| Version | Date | Description | Humain |
| :- | :- | :- | :- |
| 1.0.0 | 2024-11-26 | Instructions initiales | Charles-Edouard Bardyn |

# Instructions

## But

Générer les fichiers nécessaires pour un nouveau workflow, en s'inspirant des workflows existants.

## Besoins

IMPORTANT : Crée ces fichiers dans le dossier `_ai_workflows/factory/new_workflow/` existant, dans un sous-dossier `_generated/<nom_du_workflow>/` :
- Un nouveau fichier `run.md`
- Un dossier `instructions` contenant un fichier `instructions_v1.0.0.md`

Structure de dossier à créer :
  ```
  _ai_workflows/factory/new_workflow/_generated/
    <nom_du_workflow>/
      instructions/
        instructions_v1.0.0.md
      run.md
  ```
Ne modifie PAS de fichier existant !

## Specifications

N/A

## Tâches

### 0. Collecte des inputs
- Demande à l'utilisateur tous les inputs nécessaires :
  * Description : Description du workflow
  * Contexte : @Codebase pour l'accès aux workflows existants
- Ne fais RIEN tant que TOUS les inputs n'ont pas été fournis.

### 1. Génération des fichiers du workflow
En s'inspirant des workflows existants dans @Codebase.

### 2. Validation
Vérifie :
- [ ] La cohérence du workflow par rapport à la description donnée
