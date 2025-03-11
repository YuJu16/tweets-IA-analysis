import sys
sys.path.append("./Scripts")

import cleaning
import enrichment
import kpi_visualization

# Définition du chemin du fichier
file_path = "./Scripts/filtered_tweets_engie.csv"

# Étape 1 : Nettoyage des données
df = cleaning.clean_data(file_path)

# Étape 2 : Enrichissement des données
df = enrichment.enrich_data(df)

# Étape 3 : Génération des KPI et visualisations
kpi_visualization.generate_kpi_and_visuals(df)

# Sauvegarde du fichier final
df.to_csv("./Scripts/filtered_tweets_engie_final.csv", index=False, sep=';')
