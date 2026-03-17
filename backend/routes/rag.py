from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def rag(query: str):
    return {"response": "dummy answer"}