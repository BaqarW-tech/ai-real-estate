🇸🇦 JeddahVision AI: Real Estate Valuation & Investment Engine

![alt text](https://img.shields.io/badge/Python-3.8+-blue.svg)


![alt text](https://img.shields.io/badge/Streamlit-Deployment-red.svg)


![alt text](https://img.shields.io/badge/ML-Random%20Forest-green.svg)


![alt text](https://img.shields.io/badge/Market-Jeddah,%20KSA-orange.svg)

📌 Project Overview

JeddahVision AI is a Machine Learning-powered platform designed to provide instant property valuations in Jeddah, Saudi Arabia. By integrating real estate market data with geospatial proximity to Vision 2030 Giga-projects (such as the Jeddah Central Project and the Obhur Waterfront development), this tool helps investors and developers make data-driven decisions.

🎯 The "Standout" Feature

Unlike generic price predictors, this engine calculates an "Investment Score" based on the property's distance to the Red Sea coastline and upcoming urban transformation zones, aligning with the Kingdom's National Transformation Program.

🚀 Key Features

Smart Valuation: Predicts property prices based on District, Area (Sqm), and proximity to key landmarks.

Vision 2030 Proximity Analysis: Automatically identifies if a property is in a "High-Growth" zone.

Interactive Dashboard: A professional Streamlit interface featuring dynamic maps and market metrics.

Localized Insights: Built specifically for the Jeddah market using SAR (Saudi Riyal) and local district mapping.

🛠️ Tech Stack

Language: Python 3.9

Modeling: Scikit-Learn (Random Forest Regressor)

Data Handling: Pandas, NumPy

Deployment: Streamlit Cloud

Environment: Google Colab (Training Pipeline)

📊 Business Impact

This project solves three major challenges in the KSA real estate market:

Price Transparency: Provides a baseline for buyers and sellers in a rapidly changing market.

Investment De-risking: Highlights properties within the "Jeddah Central" influence zone.

Operational Efficiency: Automates the initial appraisal process for real estate agents.

📁 Repository Structure
code
Bash
download
content_copy
expand_less
├── app.py                # The Streamlit web application code
├── jeddah_model.pkl      # Trained Random Forest model (The Brain)
├── districts.pkl         # Encoded mapping of Jeddah districts
├── requirements.txt      # List of dependencies for cloud deployment
└── jeddah_real_estate.csv # The dataset used for training
⚙️ How to Run Locally

Clone the repository:

code
Bash
download
content_copy
expand_less
git clone https://github.com/YOUR_USERNAME/jeddah-real-estate-ai.git

Install dependencies:

code
Bash
download
content_copy
expand_less
pip install -r requirements.txt

Run the application:

code
Bash
download
content_copy
expand_less
streamlit run app.py
📈 Future Roadmap

Phase 2: Integrate Arabic Language Support (RTL Design).

Phase 3: Scrape live data from Aqar/Bayut for real-time price updates.

Phase 4: Add a "Mortgage Calculator" based on SAMA (Saudi Central Bank) regulations.

👔 Contact
BaqarW-tech 

Developed with the goal of contributing to the technological advancement of the Saudi Real Estate Sector under Vision 2030.
