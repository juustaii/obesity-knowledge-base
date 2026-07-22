from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from agent.rag_engine import RAGEngine
from crawler.crawler import CrawlerManager

load_dotenv()

app = FastAPI(
    title="Obesity Knowledge Base API",
    description="Clinical Q&A agent with RAG and web crawler",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize RAG engine and crawler
rag_engine = RAGEngine()
crawler_manager = CrawlerManager()

class Question(BaseModel):
    query: str
    max_sources: int = 3

class CrawlerConfig(BaseModel):
    keywords: list = None
    sources_enabled: dict = None
    min_relevance_score: float = None
    update_frequency_days: int = None

class HealthResponse(BaseModel):
    status: str
    rag_ready: bool
    crawler_active: bool

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Check system health status"""
    return {
        "status": "operational",
        "rag_ready": rag_engine.is_initialized(),
        "crawler_active": crawler_manager.is_active()
    }

@app.post("/api/v1/ask")
async def ask_clinical_question(question: Question):
    """
    Ask a clinical question about obesity management.
    Returns answer with source citations.
    """
    try:
        result = await rag_engine.query(
            question.query,
            max_sources=question.max_sources
        )
        return {
            "question": question.query,
            "answer": result["answer"],
            "sources": result["sources"],
            "confidence": result["confidence"],
            "disclaimer": "This is for educational purposes. Consult healthcare providers for medical advice."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/crawler/status")
async def get_crawler_status():
    """
    Get current crawler status and activity log
    """
    return crawler_manager.get_status()

@app.post("/api/v1/crawler/config")
async def update_crawler_config(config: CrawlerConfig):
    """
    Update crawler configuration
    """
    try:
        crawler_manager.update_config(config.dict(exclude_none=True))
        return {
            "status": "success",
            "message": "Crawler configuration updated",
            "new_config": crawler_manager.get_config()
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/v1/crawler/run")
async def trigger_crawler():
    """
    Manually trigger crawler run
    """
    try:
        job_id = await crawler_manager.run_crawl()
        return {
            "status": "started",
            "job_id": job_id,
            "message": "Crawler job initiated"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/sources")
async def list_sources():
    """
    Get list of all indexed sources
    """
    return {
        "total_sources": rag_engine.get_source_count(),
        "sources": rag_engine.get_all_sources()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
