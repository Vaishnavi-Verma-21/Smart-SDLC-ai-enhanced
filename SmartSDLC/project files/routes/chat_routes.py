from fastapi import APIRouter, Form
from utils import ai_chatbot
# assuming you have this
from services.ai_chat_service import generate_response

router = APIRouter(prefix="/chat", tags=["Chatbot"])

@router.post("/ask")
async def ask_chatbot(question: str = Form(...)):
    return {"response": ai_chatbot(question)}
