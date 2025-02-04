# routes/auth.py
from fastapi import APIRouter
from database import users_db, generate_api_key
from models import User

router = APIRouter()

@router.post("/signup")
def signup(user: User):
    api_key = generate_api_key()
    users_db[user.name] = {
        "age": user.age,
        "capital": user.capital,
        "risk_capacity": user.risk_capacity,
        "api_key": api_key
    }
    return {"message": "Signup successful", "api_key": api_key}
