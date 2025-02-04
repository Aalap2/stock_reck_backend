# utils/fetch_nse.py
import requests
from config import NSE_API_URL, HEADERS

def fetch_nse_stock(ticker: str):
    url = NSE_API_URL + ticker
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    return {"error": "Unable to fetch data"}
