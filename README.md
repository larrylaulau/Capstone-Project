# Capstone-Project
# 🪙 XAU/USD Gold Price Analytics & Forecasting (2004-2026)
**Capstone Project - Data Science & Generative AI**

## 📌 Project Overview
This project demonstrates a full-stack data science workflow to analyze and predict Gold (XAU/USD) prices. It covers the entire pipeline from **ETL (SQL/Python)**, **Exploratory Data Analysis (EDA)**, to **Machine Learning (XGBoost/LSTM)**, concluding with an **AI-driven Market Advisor Demo**.

---

## 🚀 Key Features & Innovation
- **Robust ETL Pipeline**: Automated cleaning and feature engineering of 20+ years of tick/daily data.
- **Predictive Modeling**: Comparison between traditional ML (Random Forest/XGBoost) and Deep Learning (LSTM).
- **Generative AI Demo**: A specialized "AI Market Strategist" that interprets technical indicators and generates natural language investment summaries.
- **2026 Market Context**: Analysis of the historic gold surge leading into early 2026.

---

## 🛠️ Tech Stack
- **Data**: Python (Pandas, NumPy), SQL (SQLite)
- **ML/DL**: Scikit-learn, XGBoost, PyTorch/TensorFlow
- **GenAI**: OpenAI GPT-4o (Implementation via Demo scripts)
- **Visualization**: Matplotlib, Seaborn, Tableau/Power BI

---

## 📂 Project Structure
```text
├── data/               
│   ├── raw/            # [Action Required] Place Kaggle CSV here
│   └── processed/      # Cleaned data and technical indicators
├── notebooks/          
│   ├── 01_EDA.ipynb    # Visualizing 20-year trends & volatility
│   └── 02_Modeling.ipynb # Training XGBoost & LSTM models
├── src/                
│   ├── data_loader.py  # ETL process (SQL/CSV)
│   └── ai_demo.py      # Generative AI "Market Strategist" Demo script
├── reports/            # Final Report (PDF) & Presentation (PPT)
└── README.md
