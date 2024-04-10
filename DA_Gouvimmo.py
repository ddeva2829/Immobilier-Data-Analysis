
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
        page_title="Étude de l'immobilier en France",
        page_icon="🏠",  # Replace this with the path to your icon file
        layout="wide"
    )

st.title("ETUDE DU MARCHE DE L’IMMOBILIER EN FRANCE")
st.sidebar.title("🏠 Etude Immobilier")
pages=["Le Projet", "Le Jeu de données", "DataVizualization", "Modélisation","Machine Learning","Conclusion & Perspective"]
page=st.sidebar.radio("Aller vers", pages)

col = st.columns((4.5, 2), gap='medium')

with col[0]:
 if page == pages[0] : 
  st.write("### Introduction Du Projet")
  st.write("""
 <div style="text-align: justify;">
  <p>  Ce projet consiste à analyser le marché immobilier français afin de comprendre ses tendances, anticiper les évolutions futures et conseiller les parties prenantes. Il inclut la collecte, le nettoyage et l'analyse des données de 2018 à 2023, en tenant compte de facteurs tels que les politiques économiques, les taux d'intérêt, la démographie et les avancées technologiques. Sur le plan scientifique, il applique des méthodes statistiques et d'apprentissage automatique pour analyser les tendances, prédire les développements futurs et fournir des insights pour la prise de décision.

    Dans le prétraitement des données, une normalisation et le traitement des valeurs manquantes et aberrantes sont effectués. Le feature engineering permettra de créer de nouvelles variables pertinentes pour l'analyse, comme le prix au mètre carré et la catégorisation des DPE en fonction de l'évolution des prix des biens par régions. Des outils de visualisation tels que Matplotlib, Seaborn et Power BI seront utilisés pour présenter l'analyse et représenter les tendances et les relations dans les données. Des analyses statistiques aideront à déterminer les facteurs influençant le marché immobilier pour une meilleure prise de décisions.

    </p>
 </div>
    """, unsafe_allow_html=True)
  
 if page == pages[1] : 
    df=pd.read_csv("Valdoise_data.csv",sep=',',low_memory=False)
    st.dataframe(df.head(10))
    st.write(df.shape)
    
 if page == pages[2] : 
    @st.cache_data
    def charger_donnees():
      df = pd.read_csv('Valdoise_data.csv')
      df['nombre_pieces_principales'] = pd.to_numeric(df['nombre_pieces_principales'], errors='coerce')
      # Assurez-vous de convertir les colonnes nécessaires en numérique si elles ne le sont pas déjà
      df['valeur_fonciere'] = pd.to_numeric(df['valeur_fonciere'], errors='coerce')
      df['surface_reelle_bati'] = pd.to_numeric(df['surface_reelle_bati'], errors='coerce')
      # Calcul du Prix au m²
      df['Prix au m²'] = df['valeur_fonciere'] / df['surface_reelle_bati']
      return df
    
    df = charger_donnees()

    df_filtered = df[(df['nombre_pieces_principales'] != 0) & (df['nombre_pieces_principales'] <= 15)]

    # Display the charts based on user selection
    # Select Chart Type
    chart_type = st.sidebar.radio("Choisir le type de graphique:", (
        'Distribution de "type_local_x"',
        'Distribution des Pieces Principales',
        'Surface Distribution par Type',
        'Value Distribution par Type',
        'Globale Value Distribution',
        'Distribution du Prix au m²',
        
     ))

    if chart_type == 'Distribution de "type_local_x"':
      fig, ax = plt.subplots()
      sns.countplot(x='type_local_x', data=df_filtered, palette='deep', ax=ax)
      st.pyplot(fig)

    elif chart_type == 'Distribution des Pieces Principales':
      fig, ax = plt.subplots()
      sns.countplot(x='nombre_pieces_principales', data=df_filtered, palette='deep', ax=ax)
      st.pyplot(fig)

    elif chart_type == 'Surface Distribution par Type':
      fig = plt.figure()
      sns.boxplot(x='type_local_x', y='surface_reelle_bati', data=df_filtered)
      plt.xticks(rotation=45)
      st.pyplot(fig)

    elif chart_type == 'Value Distribution par Type':
      fig = plt.figure()
      sns.boxplot(x='type_local_x', y='valeur_fonciere', data=df_filtered)
      plt.xticks(rotation=45)
      st.pyplot(fig)

    elif chart_type == 'Globale Value Distribution':
      fig, ax = plt.subplots()
      sns.histplot(df['valeur_fonciere'], bins=50, kde=False)
      st.pyplot(fig)

    elif chart_type == 'Distribution du Prix au m²':
      df_filtered['Prix au m2'] = df_filtered['valeur_fonciere'] / df_filtered['surface_reelle_bati']
      fig, ax = plt.subplots()
      sns.distplot(df_filtered['Prix au m2'].dropna(), bins=50, kde=False)
      st.pyplot(fig)

      
   
 with col[1]:
  with st.expander('About', expanded=True):
        st.write('''
            - Data: [Data.Gouv.fr](https://files.data.gouv.fr/geo-dvf/latest/csv/).
            - :orange[**DataScientest**]: Ce projet a été réalisés dans le cadre de notre formation en data science via l'organisme Datascientest.
            - :green[**Participants**]: Éric LOUGUET Marc DEVADEVAN Mohamed KEITA
                 ''')
            