# routes/stocks.py
from fastapi import APIRouter, Depends, HTTPException
from utils.fetch_nse import fetch_nse_stock
from database import validate_api_key

router = APIRouter()

@router.get("/nse/stock/{ticker}")
def get_nse_stock_data(ticker: str, api_key: str):
    user = validate_api_key(api_key)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return {"symbol": ticker, "data": fetch_nse_stock(ticker)}

@router.get("/nse/live/{ticker}")
def get_nse_live_stock(ticker: str, api_key: str):
    user = validate_api_key(api_key)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    data = fetch_nse_stock(ticker)
    if "priceInfo" in data:
        return {"symbol": ticker, "price": data["priceInfo"]["lastPrice"]}
    return {"error": "Live price not available"}
