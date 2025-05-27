| Version | Date | Description | Humain |
| :- | :- | :- | :- |
| 1.0.0 | 2024-12-17 | Instructions initiales | Charles-Edouard Bardyn |

# Instructions

## But

Analyser une FAQ existante, identifier les questions non couvertes, et générer des suggestions de réponses pour enrichir la FAQ.

## Besoins

- Extraction des paires Q&R existantes depuis une URL
- Analyse des nouvelles questions utilisateurs
- Génération de suggestions pertinentes

## Spécifications

### Style d'écriture des réponses suggérées
- Professionnel et clair
- Concis mais complet
- Cohérent avec le style des réponses existantes
- Structuré pour une lecture facile

### Output

IMPORTANT : Crée tous tes fichiers dans le dossier existant `2024-12_workflows_ia_code/_ai_workflows/code_based/faq_analysis/_text/` et sous-dossier `_output/`. Pas ailleurs.

## Tâches

### 0. Collecte des inputs
- Demande à l'utilisateur tous les inputs nécessaires :
  * URL de la FAQ à analyser
  * Fichier markdown contenant les nouvelles questions
- Ne fais RIEN tant que TOUS les inputs n'ont pas été fournis.

### 1. Extraction de la FAQ existante (`1_faq_existante.md`)
- Analyse la page web fournie
- Extrait TOUTES les paires questions-réponses
- Structure les données ainsi :
  ```markdown
  # FAQ Existante
  
  ## Questions-réponses extraites
  ### Q1: <question>
  <réponse>
  
  ### Q2: <question>
  <réponse>

  Etc.
  ```

### 2. Analyse des nouvelles questions (`2_analyse_questions.md`)
- Compare avec la FAQ existante
- Identifie les questions non couvertes
- Évalue la pertinence pour la FAQ
- Enregistre dans ce format :
  ```markdown
  # Analyse des nouvelles questions
  
  ## Questions non couvertes
  1. <question>
     - Pertinence: <score/5>
     - Justification: <pourquoi cette question est pertinente>
  
  ## Questions similaires aux existantes
  1. <nouvelle question>
     - Correspond à: Q<n> dans la FAQ existante
     - Différences: <analyse des nuances>
  ```
- N'oublie aucune question !

### 3. Génération des suggestions (`3_suggestions.md`)
Pour chaque nouvelle question pertinente :
- Génère 3 propositions de réponses différentes
- Adapte le style au ton de la FAQ existante
- Enregistre dans ce format :
  ```markdown
  # Suggestions de réponses
  
  ## Question 1: <question>
  
  ### Suggestion 1.1
  <réponse>
  
  ### Suggestion 1.2
  <réponse>
  ```

### 4. Production du rapport (`4_rapport.md`)
Crée un rapport consolidant :
- Résumé de l'analyse
- Liste des nouvelles questions
- Suggestions de réponses
- Recommandations de priorisation basées sur les scores de pertinence

### 5. Validation
Vérifie :
- [ ] Extraction complète de la FAQ existante
- [ ] Pertinence des nouvelles questions identifiées
- [ ] Qualité et cohérence des réponses suggérées
- [ ] Format et structure du rapport