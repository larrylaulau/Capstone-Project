import pandas as pd
from sqlalchemy import create_engine

def etl_process(file_path):
    # 處理分號
    df_raw = pd.read_csv(file_path, sep=';')
    # SQL Load
    engine = create_engine('sqlite:///gold_market.db')
    df_raw.to_sql('raw_gold_prices', engine, if_exists='replace', index=False)
    # SQL Transform
    query = "SELECT * FROM raw_gold_prices WHERE Date >= '2010-01-01'"
    df = pd.read_sql(query, engine)
    df['Date'] = pd.to_datetime(df['Date'])
    return df, engine

