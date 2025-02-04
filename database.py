# database.py
import secrets
import hashlib

users_db = {}

def generate_api_key():
    return secrets.token_hex(32)  # Generate a 64-character API key

def hash_api_key(api_key: str):
    return hashlib.sha256(api_key.encode()).hexdigest()

def validate_api_key(api_key: str):
    for user, data in users_db.items():
        if data["api_key"] == api_key:
            return user
    return None
