from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext 
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os

SECRET_KEY = str(os.environ.get("SECRET_KEY"))
ALGORITHM = str(os.environ.get("ALGORITHM"))
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(raw_password, hashed_password):
    return pwd_context.verify(raw_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data:dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp" : expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt