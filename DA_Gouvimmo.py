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
pages=["Le Projet", "Exploration", "DataVizualization", "Modélisation","Machine Learning","Conclusion & Perspective"]
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
  st.subheader("Profils des Membres du Groupe :")

  st.subheader("Éric LOUGUET")
  st.write("""
 <div style="text-align: justify;">
   <p> Coordinateur de Supply Chain, cherche à comparer les conclusions du projet avec les opinions des professionnels de l'immobilier pour valider les analyses.
   </p>
 </div>        
    """, unsafe_allow_html=True)
    
  st.subheader("Marc DEVADEVAN")
  st.write("""
 <div style="text-align: justify;">         
  <p>  Expert en qualité à La Poste, vise à améliorer son expertise grâce à une formation en analyse de données pour une meilleure prise de décision et satisfaction client.
 </div>         
    """, unsafe_allow_html=True)

  st.subheader("Mohamed KEITA")
  st.write("""
 <div style="text-align: justify;">          
  <p> Conseiller financier en reconversion data analyste au sein de la banque CCF, il est en contact avec des experts métiers dans le financement immobilier et de courtages. Des benchmarks avec des projets similaires dans nos entreprises respectives n’ont pas pu être réalisés car les données n’étaient pas en open-source. Mais, une approche avec d’autres sources telles que STATISTA, seloger.com, les données de l’INSEE et de la Banque de France ont pu être possibles. 

    
   </p>
 </div>        
   
    """, unsafe_allow_html=True)
with col[1]:
  with st.expander('About', expanded=True):
        st.write('''
            - Data: [Data.Gouv.fr](https://files.data.gouv.fr/geo-dvf/latest/csv/).
            - :orange[**DataScientest**]: Ce projet a été réalisés dans le cadre de notre formation en data science via l'organisme Datascientest.
            
            ''')