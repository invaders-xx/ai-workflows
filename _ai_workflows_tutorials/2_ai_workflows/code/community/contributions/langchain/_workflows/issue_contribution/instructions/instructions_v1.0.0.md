| Version | Date | Description | Humain |
| :- | :- | :- | :- |
| 1.0.0 | 2024-11-26 | Instructions initiales | Charles-Edouard Bardyn |

# Instructions

## But

Analyser un ticket d'un projet (e.g., GitHub) et générer des instructions claires pour le résoudre, sans modifier le code source.

## Output

IMPORTANT : Crée tous tes fichiers dans le dossier existant `code/community/contributions/langchain/_workflows/issue_contribution` et sous-dossier `_<ticket_number>/`. Pas ailleurs.

## Tâches

### 0. Collecte des inputs
- Demande à l'utilisateur tous les inputs nécessaires :
  * Issue : URL du ticket
  * Code : Dossier contenant le code source du projet
  * Guidelines : Lien vers des guidelines de contribution au projet
  * Template : Template à utiliser pour créer `instructions_v1.0.0.md`
- Ne fais RIEN tant que TOUS les inputs n'ont pas été fournis.

### 1. Analyse technique (`1_technical_analysis.md`)
- Identifie le problème central
- Analyse le code impacté
- Documente les contraintes techniques
- Liste les dépendances

### 2. Propositions d'implémentation (`2_implementation_options.md`)
- Identifie 3-5 approches possibles
- Pour chaque approche :
  * Description technique
  * Avantages/Inconvénients
  * Complexité estimée
- Recommande la meilleure approche

### 3. Instructions de contribution (`instructions_v1.0.0.md` dans un sous-dossier `3_contribution_workflow/`)
- Crée le fichier d'instructions selon le template donné
- Inclus des tests et critères de validation

### 4. Validation finale
- Vérifie la cohérence des documents
- Confirme le respect des guidelines
- Valide la complétude des instructions
- Critères à valider :
  * [ ] Template respecté
  * [ ] Impact sur le code existant minimisé
  * [ ] Guidelines du projet respectées
  * [ ] Tests bien définis
