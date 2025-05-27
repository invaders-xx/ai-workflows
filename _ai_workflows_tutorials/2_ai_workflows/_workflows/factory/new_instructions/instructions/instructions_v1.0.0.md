| Version | Date | Description | Humain |
| :- | :- | :- | :- |
| 1.0.0 | 2024-11-26 | Instructions initiales | Charles-Edouard Bardyn |

# Instructions

## But

Générer un nouveau fichier d'instructions pour réaliser un projet, en s'inspirant des fichiers d'instructions existants.

## Besoins

IMPORTANT : Crée ceci dans le dossier `_workflows/factory/new_instructions/` existant, dans un sous-dossier `_generated/<nom_du_projet>/` :
- Un dossier `instructions` contenant un fichier `instructions_v1.0.0.md`

Structure de dossier à créer :
  ```
  _workflows/factory/new_instructions/_generated/
    <nom_du_projet>/
      instructions/
        instructions_v1.0.0.md
  ```
Ne modifie PAS de fichier existant !

## Specifications

N/A

## Tâches

### 0. Collecte des inputs
- Demande à l'utilisateur tous les inputs nécessaires :
  * Description : Description du projet
  * Template : Template de fichier d'instructions à utiliser
  * Contexte : @Codebase pour l'accès aux instructions existantes
- Ne fais RIEN tant que TOUS les inputs n'ont pas été fournis.

### 1. Génération du fichier d'instructions
A partir du template, en s'inspirant aussi des fichiers d'instructions existants dans @Codebase.

### 2. Validation
Vérifie :
- [ ] La conformité du fichier d'instructions par rapport au template