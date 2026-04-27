# =============================================================================
# main.py — FastAPI entry point cho AI Gia Sư
# =============================================================================
# Vai trò: Khởi động server, định nghĩa API endpoints, kết nối tất cả modules

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import modules (sẽ implement sau)
# from agent.tutor_agent import TutorAgent
# from monitoring.logging_config import setup_logging

# Setup logging
# setup_logging()
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="AI Gia Sư Toán",
    description="Hướng dẫn giải bài toán bằng gợi ý, không cho đáp án thẳng",
    version="0.1.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response models
class ChatRequest(BaseModel):
    question: str
    grade: str  # "10" | "11" | "12"
    session_id: str | None = None

class ChatResponse(BaseModel):
    response: str
    confidence: float
    chunks_used: list[str]
    escalated: bool

# API Endpoints

@app.get("/")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "ok",
        "service": "AI Gia Sư Toán",
        "version": "0.1.0"
    }

@app.post("/chat")
async def chat(request: ChatRequest) -> ChatResponse:
    """
    Main chat endpoint
    
    Nhận câu hỏi từ học sinh, xử lý qua tutor_agent, trả về gợi ý.
    
    TODO (Day 3): Implement tutor_agent.process()
    """
    try:
        # TODO: Gọi tutor_agent.process(request.question, request.grade)
        # response = await tutor_agent.process(request.question, request.grade)
        
        # Placeholder response
        return ChatResponse(
            response="[Placeholder] Gợi ý sẽ được implement trong Day 3",
            confidence=0.0,
            chunks_used=[],
            escalated=False
        )
    except Exception as e:
        logger.error(f"Error processing chat: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/feedback")
async def feedback(session_id: str, rating: int, comment: str = ""):
    """
    Ghi nhận feedback từ học sinh
    
    TODO (Day 13): Implement feedback logging
    """
    return {"status": "feedback received"}

# Startup event
@app.on_event("startup")
async def startup_event():
    """Khởi tạo khi server start"""
    logger.info("Starting AI Gia Sư server...")
    # TODO (Day 7): Load knowledge_base
    # TODO (Day 13): Initialize tracing
    logger.info("Server started successfully")

# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup khi server shutdown"""
    logger.info("Shutting down AI Gia Sư server...")
    # TODO: Cleanup resources

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
