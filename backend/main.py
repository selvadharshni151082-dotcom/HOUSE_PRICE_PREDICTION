from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
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


# Find project folder
BASE_DIR = Path(__file__).resolve().parent.parent


# Find model file
MODEL_PATH = BASE_DIR / "model" / "house_price_model.pkl"


# Find frontend folder
FRONTEND_DIR = BASE_DIR / "frontend"


# Serve frontend files
app.mount(
    "/static",
    StaticFiles(directory=FRONTEND_DIR),
    name="static"
)


# Load trained machine learning model
model = joblib.load(MODEL_PATH)


# Input data structure
class HouseData(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    stories: int
    parking: int


# Home page
@app.get("/")
def home():
    return FileResponse(
        FRONTEND_DIR / "index.html"
    )


# Prediction API
@app.post("/predict")
def predict_price(house: HouseData):

    # Prepare input data
    input_data = [[
        house.area,
        house.bedrooms,
        house.bathrooms,
        house.stories,
        house.parking
    ]]


    # Make prediction
    prediction = model.predict(input_data)


    # Get predicted price
    predicted_price = prediction[0]


    # Return prediction
    return {
        "predicted_price": round(predicted_price, 2)
    }