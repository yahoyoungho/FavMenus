from fastapi import FastAPI, Depends
from . import crud

app = FastAPI()

@app.get("/restaurants/")
async def read_restaurants(skip: int = 0, limit: int = 10):
    restaurants = await crud.get_restaurants(skip=skip, limit=limit)
    return restaurants
