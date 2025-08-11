from fastapi import FastAPI
from app.api import dialogue

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Backend api running..."}

app.include_router(dialogue.router)