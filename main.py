# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth, stocks, recommendations

app = FastAPI()
@app.get("/")
def home():
    return {"message": "FastAPI is running!"}

@app.get("/nse/stock/{ticker}")
def get_nse_stock_data(ticker: str):
    return {"symbol": ticker, "price": 1234.56} 
# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routes
app.include_router(auth.router)
app.include_router(stocks.router)
app.include_router(recommendations.router)

# Run with: uvicorn main:app --reload
