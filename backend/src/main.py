from datetime import datetime, timedelta, timezone
from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


import uvicorn
import crud
from data_struct import auth_var_struct, user_var_struct, restaurant_var_struct


# SECRET_KEY = "d8f4a0314a7705eae9e181d090437a3d3688196878fec417760c9ea4f392f094"
SECRET_KEY = str(os.environ.get("SECRET_KEY"))
# ALGORITHM = "HS256"
ALGORITHM = str(os.environ.get("ALGORITHM"))
ACCESS_TOKEN_EXPIRE_MINUTES = 120
# ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")

# todo: replace db to db query result of 
fake_users_db = {
    "johndoe": {
        "username": "johndoe@example.com",
        "first_name":"John",
        "last_name":"Doe",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    },
    "alice": {
        "username": "alice@example.com",
        "first_name": "Alice",
        "last_name": "Wonderland",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
app = FastAPI()

def verify_password(raw_password, hashed_password):
    return pwd_context.verify(raw_password, hashed_password)

def get_password_hash(password):
    return  pwd_context.hash(password)

def get_user(db, username:str):
    if username in db:
        user_dict = db[username]
        return user_var_struct.UserInDB(**user_dict)

def authenticate_user(fake_db, username:str, password:str):
    user=get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data:dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp" : expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail="Could not validate credentials",
                                         headers={"WWW-Authenticate":"Bearer"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload["sub"]
        if username is None:
            raise credential_exception
        token_data = auth_var_struct.TokenData(username=username)
    except JWTError:
        raise credential_exception
    user = get_user(fake_users_db, username=str(token_data.username))
    if user is None:
        raise credential_exception
    return user



async def get_current_active_user(
        curernt_user: Annotated[user_var_struct.User, Depends(get_current_user)]):
    if curernt_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive User")
    return curernt_user

# =========================== API LIST ==========================

# ========================== POST METHOD ========================
@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> auth_var_struct.Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate":"Bearer"}
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return auth_var_struct.Token(access_token=access_token, token_type="bearer")
    # if not user_dict:
    #     raise HTTPException(status_code=400, detail="Incorrect User name or passowrd")
    # user = UserInDB(**user_dict)
    # hashed_password = fake_hash_password(form_data.password)
    # if not hashed_password == user.hashed_password:
    #     raise HTTPException(status_code=400, detail="Incorrect User name or passowrd")
    # return {"access_token": user.username, "token_type":"bearer"}
# TODO: upload_restaurant

# TODO: upload_menu

# ========================== GET METHOD ========================

@app.get("/restaurants/")
async def read_restaurants(skip: int = 0, limit: int = 10):
    restaurants = await crud.get_restaurants(skip=skip, limit=limit)
    return restaurants

# TODO: read_restaurants_submitted_by_user(user_id)

# TODO: read_menus_from_restaurant(restautrant_id)





@app.get("/users/me", response_model=user_var_struct.User)
async def read_users_me(current_user: Annotated[user_var_struct.User, Depends(get_current_active_user)]):
    return current_user

@app.get("/users/me/items/")
async def read_own_items(current_user:Annotated[user_var_struct.User, Depends(get_current_active_user)]):
    return [{"item_id":"foo", "owner":current_user.username}]

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8000, log_level="debug", reload=True)