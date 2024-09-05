from fastapi import APIRouter, HTTPException
from huggingface_hub import InferenceClient
import os
from models.request_models import ChatRequest

router = APIRouter()


HF_API_KEY = os.getenv("HF_API_KEY")
if not HF_API_KEY:
    raise ValueError("Hugging Face API key is not set in the environment variables")

client = InferenceClient(
    model="HuggingFaceH4/zephyr-7b-beta",
    token=HF_API_KEY,
)



@router.post("/")
async def chat(request: ChatRequest):
    try:
        messages = [{"role": "user", "content": request.text}]
        response_content = ""

        # Streaming the response
        for message in client.chat_completion(
            messages=messages,
            max_tokens=500,
            stream=True,
        ):
            response_content += message.choices[0].delta.content

        return {"response": response_content}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
