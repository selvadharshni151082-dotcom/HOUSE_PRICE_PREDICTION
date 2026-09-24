from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
from pathlib import Path


# Create FastAPI application
app = FastAPI()


# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Find model file
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "house_price_model.pkl"


# Load trained model
model = joblib.load(MODEL_PATH)


# Input data structure
class HouseData(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    stories: int
    parking: int


# Home route
@app.get("/")
def home():
    return {
        "message": "House Price Prediction API is running"
    }


# Prediction API
@app.post("/predict")
def predict_price(house: HouseData):

    input_data = [[
        house.area,
        house.bedrooms,
        house.bathrooms,
        house.stories,
        house.parking
    ]]

    prediction = model.predict(input_data)

    predicted_price = prediction[0]
    return {
        "predicted_price": round(predicted_price, 2)
    }