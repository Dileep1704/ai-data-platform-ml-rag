from fastapi import FastAPI

# Import routes
from backend.routes import ingest, predict, rag

# ⭐ IMPORTANT: Import DB + Models
from backend.database import engine, Base
from backend.models import UserData

# Create tables in PostgreSQL
Base.metadata.create_all(bind=engine)

# Initialize app
app = FastAPI(title="AI Data Platform")

# Include routes
app.include_router(ingest.router, prefix="/ingest")
app.include_router(predict.router, prefix="/predict")
app.include_router(rag.router, prefix="/rag")

# Home route
@app.get("/")
def home():
    return {"message": "AI Data Platform Running Successfully 🚀"}