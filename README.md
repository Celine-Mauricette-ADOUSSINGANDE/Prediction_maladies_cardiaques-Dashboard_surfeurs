# 🧠❤️ Détection de maladies cardiaques & Dashboard Surf 🌊

Ce dépôt contient deux projets data complets : 

1. **Un protocole de détection de maladies cardiaques** basé sur l’analyse statistique et le machine learning.  


2. **Un dashboard interactif pour une école de surf**, alimenté par du web scraping et développé avec *flexdashboard* (R).

---

# ❤️ Partie 1 — Détection de maladies cardiaques

## 🎯 Objectif
Développer un **protocole médical minimaliste et fiable** permettant de prédire la présence d’une maladie cardiaque à partir du dataset *Heart_Disease_Prediction.csv*.

---

## Étapes réalisées

### 1. Exploration & nettoyage des données
- Vérification du nombre de lignes et colonnes  
- Correction des types de variables  
- Gestion des valeurs manquantes  
- Suppression des doublons  

### 2. Analyse descriptive
- Statistiques : Q1, Q3, moyenne, médiane, variance  
- Visualisations : histogrammes, distributions  
- Interprétation médicale des tendances  

### 3. Analyse multivariée
- Matrice de corrélation  
- Identification des variables les plus liées à la maladie  

### 4. Tests statistiques
Pour chaque variable :  
- Sélection du test adapté (χ², t-test…)  
- Analyse de son influence sur la maladie  

### 5. Construction du protocole médical
- Sélection des variables les plus discriminantes  
- Proposition d’un protocole optimal minimisant le nombre de tests  

### 6. Bonus : Arbre de décision
- Construction d’un modèle CART  
- Comparaison avec le protocole manuel  

### 7. Bonus : Présentation
- Synthèse claire et pédagogique destinée à des médecins généralistes  

---

# 🌊 Partie 2 — Dashboard de conditions de surf

## 🎯 Objectif
Créer un **dashboard dynamique** permettant à une école de surf de visualiser les meilleures conditions de la semaine (vagues, vent, orientation).

---

## Étapes réalisées

### 1. Web scraping
Extraction automatique depuis :  
`https://www.surf-report.com/meteo-surf/lacanau-s1043.html`

Données collectées :
- Date  
- Heure  
- Taille des vagues  
- Vitesse du vent  
- Direction du vent  

### 2. Librairie Python : `surf_scrap`
Une fonction unique permettant :
- de scraper n’importe quelle URL surf-report  
- de générer automatiquement un fichier CSV  
- de choisir l’emplacement d’enregistrement  

### 3. Script Python d’exécution
- Permet d’appeler la librairie (surf-scrap-cli) depuis le terminal  

### 4. Dashboard R (flexdashboard)
Contenu :
- Graphique de la taille moyenne des vagues  
- Graphique de la vitesse du vent  
- Tableau récapitulatif (jour, heure, vagues, vent)  
- Encadré : meilleur moment pour surfer  
- Encadré : plus grosse vague de la semaine  
- Jauge de qualité de la mer  

Critères de qualité :
- Vague ≥ 1.0 m  
- Vent ≤ 50 km/h  
- Vent venant du Nord (mot-clé “Nord”)  

---

# 📂 Structure du dépôt

 Prediction_maladies_cardiaques-Dashboard_surfeurs
│
├── ❤️_Part_1:Heart_Disease/
│   ├── data/
│   ├── notebooks/
│   └── presentation/
│
├── 🌊_Part_2:Surf_Dashboard/
│   ├── surf_scrap_project/
│
└── README.md



🚀 **Technologies utilisées**

- Python (pandas, numpy, matplotlib, seaborn, scipy, scikit-learn, requests, BeautifulSoup)

- R (flexdashboard, tidyverse, plotly, DT)


👩‍💻 **Auteure**

Céline Adoussingande 

Étudiante en Data Science & Économétrie
Alternante Chargée d'études - Intelligence de la donnée – SFR

📬 **Contact**

📧 Email : mauriceteadoussingande@yahoo.com 

🔗 LinkedIn : https://www.linkedin.com/in/céline-adoussingande