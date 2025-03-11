import pandas as pd
import re

def enrich_data(df):
    # Extraction de l'heure uniquement au format HH:MM:SS
    df['heure'] = df['created_at'].dt.strftime('%H:%M:%S')
    
    # Ajout d'une colonne pour la longueur du texte du tweet
    df['longueur_texte'] = df['full_text'].astype(str).map(len)
    
    # Définition des mots-clés à analyser
    mots_cle = ["pas", "mois", "fait", "depuis", "service", "rien", "problème", "erreur", "panne"]
    
    # Fonction de comptage des mots-clés distincts dans un tweet
    def compter_mots_cle(text, keywords):
        if pd.isna(text):  # Vérifie si le texte est vide
            return 0
        mots = set(re.findall(r'\b\w+\b', text.lower()))
        return sum(mot in keywords for mot in mots)
    
    # Création d'une colonne contenant le nombre de mots-clés détectés
    df["nombre_mots_cle"] = df["full_text"].apply(lambda x: compter_mots_cle(x, mots_cle))
    
    # Extraction des informations temporelles
    df["jour"] = df["created_at"].dt.date
    df["mois"] = df["created_at"].dt.to_period('M')
    df["jour_semaine"] = df["created_at"].dt.day_name()
    
    # Traduction des jours de la semaine en français
    jours_traduits = {
        "Monday": "Lundi", "Tuesday": "Mardi", "Wednesday": "Mercredi", "Thursday": "Jeudi",
        "Friday": "Vendredi", "Saturday": "Samedi", "Sunday": "Dimanche"
    }
    df["jour_semaine"] = df["jour_semaine"].map(jours_traduits)
    
    return df
