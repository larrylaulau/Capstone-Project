import pandas as pd
import numpy as np

def calculate_rsi(series, window=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / (loss + 1e-9)
    return 100 - (100 / (1 + rs))

def build_features(df):
    """生成機器學習所需的特徵"""
    df = df.copy()
    # 技術指標
    df['RSI'] = calculate_rsi(df['Close'])
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    df['Price_Range'] = df['High'] - df['Low']
    df['Returns'] = df['Close'].pct_change()
    
    # Target: 預測下一小時漲跌 (1=漲, 0=跌)
    df['Target'] = (df['Close'].shift(-1) > df['Close']).astype(int)
    
    # 剔除空值
    df.dropna(inplace=True)
    print(f"✅ 特徵工程完成: 當前特徵數量 {df.shape[1]}")
    return df
