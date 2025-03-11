import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def generate_kpi_and_visuals(df):
    # Calcul des KPI
    tweets_par_jour = df.groupby("jour_semaine").size().reindex([
        "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"
    ])
    
    tweets_par_mois = df.groupby("mois").size()
    
    # Génération du nuage de mots
    textes_concat = " ".join(df["full_text"].dropna().astype(str))
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(textes_concat)
    
    # Génération des graphiques
    plt.figure(figsize=(10, 6))
    tweets_par_jour.plot(kind="bar", color="skyblue", title="Volume de tweets par jour de la semaine")
    plt.ylabel('Nombre total de tweets')
    plt.show()
    
    plt.figure(figsize=(10, 6))
    tweets_par_mois.plot(kind="bar", color="crimson", title="Volume de tweets par mois")
    plt.ylabel('Nombre total de tweets')
    plt.show()
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title("Nuage de mots des tweets")
    plt.show()
