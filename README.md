
# Fait par : Jemima, Julia, Mehdi, Erwann, Ashley


# Agent IA pour Engie  

## 📌 Description du projet  
Ce projet a pour but de développer un agent IA capable d'analyser et classifier les tweets des clients d'Engie pour identifier les problèmes courants et évaluer leur degré d'urgence. Notre solution permet de catégoriser automatiquement les plaintes, d'évaluer le sentiment exprimé et de déterminer un score d'inconfort afin de prioriser les interventions du service client.
##  Objectifs

- Prétraiter et analyser les données Twitter mentionnant ENGIE
- Développer un agent IA pour catégoriser automatiquement les plaintes
- Implémenter un système d'analyse de sentiment
- Calculer un score d'inconfort pour prioriser les interventions
- Créer un tableau de bord visuel pour suivre les KPI et tendances

## 🛠️ Technologies utilisées  
- **Google AI Studio** pour l'entraînement et l'analyse de l'IA  
- **Python** pour le traitement des données  
- **Pandas** pour la manipulation des fichiers JSON et CSV  
- **API Gemini** comme inteligence artificielle  
- **Visual Studio Code** comme environnement de développement
- **modele NLP** pour l'analyse des sentiments

## 🤖 Modèles d'IA
Notre système utilise deux modèles principaux:

- **Agent de catégorisation**: Classifie les tweets en différentes catégories de problèmes (ex: "Service client injoignable", "Problèmes de facturation")
- **Analyseur de sentiment**: Évalue si le sentiment exprimé est Négatif ,positif ou Neutre

## Categories de tweets en fonction des probleme 
- **Problèmes de facturation**
     - **Pannes et urgences**
     - **Service client injoignable**
     - **Problèmes avec l’application**
     - **Délai d’intervention**

##  optimisation de tableau de bord
Notre tableau de bord présente plusieurs indicateurs clés:

-Nombre de tweets par trimestre
-Répartitions des catégorie de plaintes
-Repartition des urgences de tweets
-mots les plus frequents dans les plaintes négatives
-Score d'inconfort par types de plaintes

## 🔍 Résultats clés
- Tous les tweets analysés présentent un sentiment négatif positif ou neutre
- Les catégories de plaintes les plus fréquentes sont "Service client injoignable" et "Problèmes de facturation"
- Un score d'inconfort élevé (90/100) a été identifié pour la majorité des tweets
- Plusieurs situations urgentes nécessitent une intervention rapide

## 🔮 Améliorations futures

- Intégration d'une API en temps réel pour récupérer les nouveaux tweets
- Amélioration de la précision du modèle de sentiment avec plus de données d'entraînement
- Ajout de fonctionnalités de réponse automatique aux plaintes urgentes
- Extension de l'analyse à d'autres plateformes de médias sociaux

## 🎯 Conclusion

Ce projet d'analyse des tweets d'ENGIE démontre l'efficacité des technologies d'IA pour améliorer la gestion de la relation client. Notre agent IA permet désormais d'identifier, catégoriser et prioriser rapidement les problèmes signalés par les clients sur Twitter. Les résultats montrent une prédominance de sentiments négatifs liés principalement à l'inaccessibilité du service client et aux problèmes de facturation. Grâce à notre tableau de bord, ENGIE peut maintenant intervenir de manière proactive sur les situations les plus urgentes, améliorant ainsi la satisfaction client et optimisant ses ressources de support.