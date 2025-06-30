# routes/feedback_routes.py

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Define feedback request body model
class Feedback(BaseModel):
    name: str
    email: str
    message: str

# Feedback endpoint
@router.post("/")
def submit_feedback(feedback: Feedback):
    # Here you would normally store to DB, send email, etc.
    print(f"Received feedback from {feedback.name} ({feedback.email})")
    return {
        "status": "success",
        "message": "Feedback received",
        "data": feedback.dict()
    }
