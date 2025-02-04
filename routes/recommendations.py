# routes/recommendations.py
from fastapi import APIRouter, Depends, HTTPException
import pandas as pd
from database import validate_api_key
from utils.fetch_nse import fetch_nse_stock
from utils.indicators import calculate_indicators
from models import User

router = APIRouter()

@router.post("/recommend")
def recommend_stocks(user: User, api_key: str):
    if validate_api_key(api_key) is None:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    tickers = ["RELIANCE", "TCS", "INFY", "HDFCBANK", "ITC", "HUL", "COALINDIA", "NTPC", "POWERGRID"]
    recommendations = []
    
    for ticker in tickers:
        stock_data = fetch_nse_stock(ticker)
        if "priceInfo" not in stock_data:
            continue
        
        df = pd.DataFrame(stock_data["priceInfo"], index=[0])
        df.rename(columns={"lastPrice": "Close"}, inplace=True)
        df = calculate_indicators(df)
        
        if user.risk_capacity == "High" and df['SMA_50'].iloc[-1] > df['SMA_200'].iloc[-1] and df['RSI'].iloc[-1] < 70:
            recommendations.append(ticker)
        elif user.risk_capacity == "Medium" and df['SMA_50'].iloc[-1] > df['SMA_200'].iloc[-1] and 30 < df['RSI'].iloc[-1] < 60:
            recommendations.append(ticker)
        elif user.risk_capacity == "Low" and df['SMA_50'].iloc[-1] < df['SMA_200'].iloc[-1] and df['RSI'].iloc[-1] > 30:
            recommendations.append(ticker)
    
    return {"recommendations": recommendations}
