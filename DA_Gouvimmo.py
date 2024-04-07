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
st.sidebar.title("🏠 Sommaire")
pages=["Le Projet", "Exploration", "DataVizualization", "Modélisation","Machine Learning","Conclusion & Perspective"]
page=st.sidebar.radio("Aller vers", pages)

col = st.columns((4.5, 2), gap='medium')

with col[0]:
 if page == pages[0] : 
  st.write("### Introduction Du Projet")
  st.write("""
    L’analyse du marché de l’immobilier français est cruciale pour comprendre les tendances, anticiper les évolutions futures et conseiller les parties prenantes (investisseurs, gouvernement, acheteurs, etc.). Cette étude se place dans un contexte où le marché immobilier est influencé par divers facteurs tels que les politiques économiques, les taux d’intérêts, les mouvements démographiques et les avancées technologiques.

    D’un point de vue technique, ce projet implique la collecte, le nettoyage et l’analyse de grande quantité de données de l’année 2018 à 2023. Le traitement des données variées (prix, localisations, caractéristiques des biens, etc) croisé à des données liées au DPE, densité de la population, évolution de l’inflation nécessite des pré traitements des données et une visualisation de ces données pour une meilleure compréhension.

    Scientifiquement, ce projet implique l’application de méthodes statistiques et de machine learning pour pouvoir analyser les tendances et prédire les évolutions futures. Il s’inscrit dans une démarche d’analyse prédictive et descriptive avec pour principales objectifs:

    - D’analyser les tendances du marché en incluant la compréhension de l’évolution des prix, des volumes des ventes, des préférences des consommateurs entre 2018 et 2023, et en corrélant les données sur la nature des biens (DPE par rapport à la typologie des biens et la variation de leur prix respectifs selon leur localisation)
    - De prédire les tendances futures en utilisant les données historiques
    - D’aider à la prise de décision en fournissant des insights pour aider les décideurs dans leurs stratégies d’investissement et de politique publique

    Notre groupe est composé d’alumni déjà expert métier dans un domaine plus ou moins lié au marché de l’immobilier:
    """)

  st.subheader("Éric LOUGUET")
  st.write("""
    Coordinateur Supply Chain au sein d’une PME spécialisée dans la fibre optique. Ne connaissant aucun expert métier personnellement, il n’a pu entrer en contact avec l’un d’entre eux pour affiner la problématique et les modèles sous-jacents. Cependant, il serait judicieux selon lui à la fin du projet de comparer ses conclusions avec celles d’un agent immobilier par exemple. Cela permettrait soit d’affirmer les analyses si elles vont dans le sens du point de vue d’un professionnel, ou alors si ce n’est pas le cas, voir quelles seraient les raisons de ces avis divergents.
    """)
    
  st.subheader("Marc DEVADEVAN")
  st.write("""
    Animateur Qualité Expert opérationnel relation client au sein du groupe LA POSTE.

    En tant que professionnel de la logistique et de la qualité, mon rôle est de contrôler et d'améliorer nos processus. Pour enrichir mon expertise, je pourrais bénéficier d'une formation en data analyst. Cette formation me permettrait d'ajouter une dimension analytique à mes responsabilités actuelles, en me permettant de prendre des décisions basées sur des données quantitatives et d'identifier des opportunités d'amélioration plus précises. En comprenant mieux les données liées à la satisfaction client, je pourrais proposer des solutions plus ciblées pour améliorer l'expérience client et contribuer à l'efficacité opérationnelle de notre organisation. De plus, cette formation m'offrirait des compétences transférables précieuses et élargirait les opportunités de carrière à l'avenir.
    """)

  st.subheader("Mohamed KEITA")
  st.write("""
    Conseiller financier en reconversion data analyste au sein de la banque CCF, il est en contact avec des experts métiers dans le financement immobilier et de courtages. Des benchmarks avec des projets similaires dans nos entreprises respectives n’ont pas pu être réalisés car les données n’étaient pas en open-source. Mais, une approche avec d’autres sources telles que STATISTA, seloger.com, les données de l’INSEE et de la Banque de France ont pu être possibles. 

    Dans le pré traitement des données, nous avons d’abord procédé à leur normalisation, le traitement des valeurs manquantes et aberrantes. Ainsi, le feature engineering nous aidera à créer de nouvelles variables pertinentes pour notre analyse, comme le prix au mètre carré, la catégorisation des DPE en fonction de l’évolution des prix des biens par régions, etc. 

    Nous utiliserons des outils de visualisation de Python (Matplotlib, Seaborn) et de Power BI pour présenter notre analyse et représenter les tendances et les relations dans les données. Des analyses statistiques nous permettront de déterminer les facteurs influençant le marché immobilier pour une meilleure prise de décisions. 

    """)
with col[1]:
  with st.expander('About', expanded=True):
        st.write('''
            - Data: [Data.Gouv.fr](https://files.data.gouv.fr/geo-dvf/latest/csv/).
            - :orange[**DataScientest**]: Ce projet a été réalisés dans le cadre de notre formation en data science via l'organisme Datascientest.
            
            ''')