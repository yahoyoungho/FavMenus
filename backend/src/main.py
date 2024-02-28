from fastapi import FastAPI, Depends
import uvicorn
import crud

app = FastAPI()


@app.get("/")
def read_root():
    # for testing purpose
    # todo: remove this function when necessary
    return {"Hello": "World"}


@app.get("/restaurants/")
async def read_restaurants(skip: int = 0, limit: int = 10):
    restaurants = await crud.get_restaurants(skip=skip, limit=limit)
    return restaurants


if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8000, log_level="debug", reload=True)