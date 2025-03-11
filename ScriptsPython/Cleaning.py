import pandas as pd
import re

def clean_data(file_path):
    # Chargement du fichier CSV avec gestion du séparateur
    df = pd.read_csv(file_path, delimiter=';', dtype={'id': str})
    
    # Nettoyage et conversion de l'ID en chaîne de caractères
    df['id'] = df['id'].str.replace(',', '.').astype(float).astype(int).astype(str)
    
    # Transformation de 'created_at' en datetime avec fuseau horaire
    df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce', utc=True)
    
    return df
