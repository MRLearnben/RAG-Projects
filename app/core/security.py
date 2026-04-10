from passlib.context import CryptContext
from jose import jwt
from app.core.config import SECRET_KEY

pwd = CryptContext(schemes=["bcrypt"])

def hash_password(p): return pwd.hash(p)
def verify_password(p, h): return pwd.verify(p, h)

def create_token(data):
    return jwt.encode(data, SECRET_KEY, algorithm="HS256")
