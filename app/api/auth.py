from fastapi import APIRouter
from app.core.security import hash_password, create_token

router = APIRouter()

users = {}

@router.post("/register")
def register(email: str, password: str):
    users[email] = hash_password(password)
    return {"msg": "registered"}

@router.post("/login")
def login(email: str, password: str):
    token = create_token({"sub": email})
    return {"token": token}
