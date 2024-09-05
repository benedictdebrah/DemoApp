import os
from fastapi import FastAPI
from api import chat, summarize

app = FastAPI()

HF_API_KEY = os.getenv("HF_API_KEY")
if not HF_API_KEY:
    raise ValueError("Hugging Face API key is not set in the environment variables")

app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(summarize.router, prefix="/summarize", tags=["Summarize"])

@app.get("/")
async def root():
    return {"message": "Welcome to the MrOpuni  App"}