# Capstone-Project
XAU/USD Gold Price Analytics & AI-Driven Forecasting (2004-2026)
**Data Science Capstone Project | Final Submission - Feb 2026**

## 📌 Project Overview
This project presents a modular data science pipeline designed to analyze and predict Gold (XAU/USD) price movements using 20+ years of historical hourly data. It integrates **SQL-based ETL**, **Advanced Feature Engineering**, **Random Forest Classification**, and a **Generative AI Trading Assistant Demo**.

## 🚀 Key Features (Assessment Criteria Alignment)
- **Modular ETL Pipeline**: Robust data extraction using Python and SQL (SQLite) to handle 120,000+ rows of tick data.
- **Statistical Engineering**: Implementation of RSI, SMA (20/50), and Volatility features for trend identification.
- **Machine Learning**: Random Forest Classifier for direction prediction (Up/Down) with rigorous chronological backtesting.
- **Generative AI Demo**: A "Market Strategist" GPT-4o integration that translates technical signals into human-readable trading insights.

---

## 🛠️ Technical Stack
- **Languages**: Python 3.12, SQL (SQLite)
- **Libraries**: Pandas, NumPy, Scikit-learn, SQLAlchemy, Seaborn, Matplotlib
- **AI/LLM**: OpenAI GPT-4o API (Mock Demo Implementation)
- **Version Control**: Git & GitHub

---

## 📂 Project Structure
```text
Gold-Price-Prediction/
├── src/                # Modular Source Code
│   ├── data_loader.py         # ETL & SQL Management
│   ├── feature_engineering.py  # Technical Indicators (RSI/SMA)
│   ├── model_trainer.py       # Random Forest Training & Metrics
│   └── ai_demo.py             # Generative AI Logic
├── notebooks/          
│   └── main.ipynb      # 👈 MAIN ENTRY POINT (Execution Hub)
├── data/               
│   └── raw/            # [Note] Place XAU_1h_data.csv here
├── requirements.txt    # Project Dependencies
└── README.md           # Documentation
