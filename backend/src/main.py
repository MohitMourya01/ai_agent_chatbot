from fastapi import FastAPI
import os

app = FastAPI()
MY_PROJECT = os.getenv("AI CHATBOT") or "AI CHATBOT default"
API_KEY = os.getenv("key")


@app.get("/")
async def read_root():   
    return {"Hello": "World again!!", "Project": MY_PROJECT}