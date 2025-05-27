# Analyse de FAQ : Deux Façons de Travailler avec l'IA 🚀

Vous vous demandez comment rendre vos workflows IA plus puissants ? Cet exemple montre deux façons d'analyser et d'améliorer les FAQs :
1. En utilisant des instructions textuelles avec un assistant IA
2. En utilisant du code structuré qui s'exécute de façon autonome

## Ce que fait cet exemple 🎯

Prend une FAQ existante et l'améliore en :
- Trouvant les questions sans réponse
- Analysant ce qui manque
- Suggérant de nouvelles réponses
- Créant un rapport d'amélioration complet

## Essayez les deux approches 🤝

### 1. Version texte : Rapide et interactive
Parfaite pour l'exploration et les itérations rapides.

```
_text/
├── run.md         # Quoi exécuter
├── instructions/  # Quoi faire
└── _output/       # Où vont les résultats
```

**Pour essayer :**
1. Ouvrez votre assistant IA
2. Copiez le contenu de `_text/run.md`
3. Regardez l'IA travailler sur les tâches
4. Discutez et affinez si nécessaire

### 2. Version code : Structurée et indépendante
Parfaite pour l'automatisation et plus de contrôle.

```
_code/
├── run.py             # Script Python
├── instructions.yaml  # Tâches structurées
├── config.yaml        # Paramètres IA
└── _output/           # Où vont les résultats
```

**Pour essayer :**
```bash
cd _code
python run.py
```

## ⚠️ Avant de commencer

1. **Configurez l'environnement Python**
   - Suivez le [guide d'installation](_ai_workflows_packages/ai_workflows/README.md)
   - Assurez-vous d'activer l'environnement Python après l'installation

2. **Obtenez un accès API**
   - Créez un compte gratuit sur [Groq](https://console.groq.com)
   - Générez une clé API
   - Ajoutez votre clé API dans `config.yaml` :
     ```yaml
     llm:
       type: "langchain_groq.ChatGroq"
       api_key: "votre-clé-api-ici"  # Remplacez par votre vraie clé
     ```

Besoin d'aide ? Consultez le [tutoriel](_ai_workflows_tutorials/3_ai_workflows_as_code/) pour plus d'informations.

## Comparez les résultats 📊

Les deux versions créent ces fichiers dans `_output/` :
1. `1_existing_faq.md` : Ce qui est dans la FAQ actuelle
2. `2_questions_analysis.md` : Ce qui manque
3. `3_suggestions.md` : Propositions de nouvelles réponses
4. `4_report.md` : Analyse complète

## Quand utiliser chaque approche 🤔

### La version texte est idéale quand vous :
- Voulez expérimenter rapidement
- Devez discuter des idées avec l'IA
- Souhaitez affiner les choses de manière interactive
- N'avez pas besoin d'automatisation

### La version code est meilleure quand vous :
- Voulez exécuter les choses automatiquement
- Avez besoin de plus de contrôle sur le processus
- Souhaitez intégrer avec d'autres outils
- Voulez être indépendant des assistants IA

## Comment créer le vôtre 🛠️

### Commencez par le texte
1. Regardez `_text/instructions/instructions_v1.0.0.md`
2. Voyez comment les tâches sont décrites en langage naturel
3. Notez comment les sorties sont spécifiées clairement

### Passez au code quand vous êtes prêt
1. Examinez `_code/instructions.yaml`
2. Voyez comment les mêmes tâches sont structurées
3. Notez comment les entrées et sorties sont explicites

---

<div align="center">
  <sub>Créé avec ❤️ par AI Swiss</sub>
</div>
