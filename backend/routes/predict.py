from fastapi import APIRouter
from pydantic import BaseModel
from ml_service.predict import predict

router = APIRouter()

# Define input schema
class Features(BaseModel):
    features: list

@router.post("/")
def predict_api(data: Features):
    result = predict(data.features)
    return {"prediction": result}