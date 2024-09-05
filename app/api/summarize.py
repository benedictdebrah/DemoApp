from fastapi import APIRouter, HTTPException
import requests
import os
from models.request_models import SummarizeRequest



router = APIRouter()

HF_API_KEY = os.getenv("HF_API_KEY")

if not HF_API_KEY:
    raise ValueError("Hugging Face API key is not set in the environment variables")

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

@router.post("/summarize")
def summarize(request: SummarizeRequest):
    output = query({
        "inputs": request.text,
    })
    return {"summary": output}


