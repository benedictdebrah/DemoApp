from pydantic import BaseModel

class ChatRequest(BaseModel):
    text: str

class SummarizeRequest(BaseModel):
    text: str
