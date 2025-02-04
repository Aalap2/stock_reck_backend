# models.py
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    capital: float
    risk_capacity: str
