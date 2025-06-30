from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Import route modules
from routes.ai_routes import router as ai_router
from routes.auth_routes import router as auth_router
from routes.chat_routes import router as chat_router
from routes.feedback_routes import router as feedback_router

# Create FastAPI app with metadata
app = FastAPI(
    title="SmartSDLC API",
    description="An AI-powered assistant for the Software Development Lifecycle.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat/chat")
async def chat_endpoint(request: ChatRequest):
    user_msg = request.message
    # Simulate AI response
    return {"reply": f"You asked: {user_msg}"}

# Setup CORS to allow frontend (e.g., Streamlit) to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers for modular functionality
app.include_router(ai_router, prefix="/ai", tags=["AI Functions"])
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(chat_router, prefix="/chat", tags=["Chatbot"])
app.include_router(feedback_router, prefix="/feedback", tags=["Feedback"])

# Root route
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to SmartSDLC API! Visit /docs for interactive API documentation."}
