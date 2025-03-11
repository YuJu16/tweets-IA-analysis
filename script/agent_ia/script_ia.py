import google.generativeai as genai

genai.configure(api_key="AIzaSyDQwozbhU1ZHg9PgdN0EfNdjpYNy97xR4Y")

model = genai.GenerativeModel('gemini-pro')

#prompt que j'ai créé pour l'IA
system_prompt = """
Tu es un assistant qui analyse les tweets des clients d'Engie. Ton travail est de catégoriser les tweets en fonction des problèmes mentionnés. Les catégories possibles sont :
- Problèmes de facturation
- Pannes et urgences
- Service client injoignable
- Problèmes avec l’application
- Délai d’intervention

Pour chaque tweet, tu dois :
1. Identifier la catégorie du problème.
2. Donner un score d'inconfort entre 0 et 100%.
3. Indiquer si le problème est urgent (oui ou non).
4. Analyser le sentiment du tweet (Positif, Neutre, Négatif).

**Format de sortie attendu :**
{
  "Catégorie": "Nom de la catégorie",
  "Inconfort": "Score entre 0 et 100",
  "Urgence": "true ou false",
  "Sentiment": "Positif | Neutre | Négatif"
}

**Important :**
- Ne fournis pas de conseils ou d'assistance client.
- Ne donne pas d'explications détaillées.
- Réponds uniquement au format JSON attendu.
"""

tweet = "@Engie je n'ai plus de gaz depuis 2 jours, c'est une urgence !"

response = model.generate_content(
    system_prompt + "\n\nAnalyse ce tweet : " + tweet
)

print(response.text)