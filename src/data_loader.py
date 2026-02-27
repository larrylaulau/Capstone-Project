import pandas as pd
from sqlalchemy import create_engine
import os

def run_etl(file_path):
    """
    Extract: 讀取分號分隔的 CSV
    Load: 存入 SQLite 數據庫
    Transform: SQL 過濾 2010 年後的數據
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"找不到檔案: {file_path}")

    # 1. Extract
    df_raw = pd.read_csv(file_path, sep=';')
    
    # 2. Load to SQL
    engine = create_engine('sqlite:///gold_market.db')
    df_raw.to_sql('raw_gold_prices', engine, if_exists='replace', index=False)
    
    # 3. Transform using SQL
    query = "SELECT * FROM raw_gold_prices WHERE Date >= '2010-01-01'"
    df = pd.read_sql(query, engine)
    df['Date'] = pd.to_datetime(df['Date'])
    
    print(f"✅ ETL 完成: 提取了 {len(df):,} 行數據。")
    return df

def audit_data(df):
    """數據質量檢查"""
    null_count = df.isnull().sum().sum()
    logical_err = len(df[df['Low'] > df['High']])
    print(f"🔍 Audit: {null_count} Nulls, {logical_err} Logical Errors.")
    return null_count == 0 and logical_err == 0
