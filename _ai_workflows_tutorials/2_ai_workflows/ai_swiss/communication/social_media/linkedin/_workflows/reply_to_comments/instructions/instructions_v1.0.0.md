| Version | Date | Description | Humain |
| :- | :- | :- | :- |
| 1.0.0 | 2024-11-26 | Instructions initiales | Charles-Edouard Bardyn |

# Instructions

## But

Générer des options de réponses personnalisées aux commentaires récents sur les posts LinkedIn des membres AI Swiss.

## Output

IMPORTANT : Crée tous tes fichiers dans le dossier `ai_swiss/communication/social_media/linkedin/_workflows/reply_to_comments/`, dans un sous-dossier `_generated`. Pas ailleurs.

## Besoins

- Cohérence avec le ton de chaque membre sur LinkedIn

## Spécifications

- Style d'écriture :
  * Professionnel
  * En accord avec la personne au nom de qui tu rédiges

## Documentation

N/A

## Tâches

### 0. Collecte des inputs
- Demande à l'utilisateur tous les inputs nécessaires :
  * Lien(s) de posts contenant des commentaires à traiter
  * Lien vers les posts de la personne au nom de qui tu dois rédiger des réponses
- Ne fais RIEN tant que TOUS les inputs n'ont pas été fournis.

### 1. Analyse des commentaires
- Identification des commentaires sans réponse
- Catégorisation des commentaires (question, feedback, suggestion, etc.)

### 2. Analyse du contexte
- Évaluation du ton du commentaire
- Identification des points clés à adresser

### 3. Génération des réponses (`reply_to_comments.md`)
- Rédaction de 5 réponses possibles pour chaque commentaire

### 4. Contrôle qualité
- Vérifie :
  * [ ] Ton et style en accord avec la personne au nom de qui tu rédiges
  * [ ] Longueur dans les limites LinkedIn
