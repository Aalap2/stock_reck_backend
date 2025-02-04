import requests

def fetch_nse_stock(ticker: str):
    NSE_API_URL = f"https://www.nseindia.com/api/quote-equity?symbol={ticker}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Referer": f"https://www.nseindia.com/get-quotes/equity?symbol={ticker}",
        "Accept-Language": "en-US,en;q=0.9",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    session = requests.Session()
    session.get("https://www.nseindia.com", headers=headers)  # Fetch cookies
    response = session.get(NSE_API_URL, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    return {"error": f"Unable to fetch data, status code {response.status_code}"}
