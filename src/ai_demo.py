def get_mock_ai_insight(price, rsi, pred_label):
    """
    用於 Presentation 的 AI 模擬輸出 (Mock Demo)
    """
    prediction = "Bullish (Up)" if pred_label == 1 else "Bearish (Down)"
    
    insight = f"""
    [AI Market Strategist Demo]
    Current Gold Price: ${price:.2f}
    RSI: {rsi:.2f}
    Model Forecast: {prediction}
    
    Analysis: The Random Forest model indicates a {prediction} bias for the next hour. 
    With an RSI of {rsi:.2f}, the market shows {'overbought' if rsi > 70 else 'balanced'} momentum. 
    Recommendation: Monitor price action near the 20-period SMA for confirmation.
    """
    return insight
