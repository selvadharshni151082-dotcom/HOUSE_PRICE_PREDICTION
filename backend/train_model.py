import pandas as pd
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


# Get project folder path
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset path
DATASET_PATH = BASE_DIR / "dataset" / "house_data.csv"

# Model save path
MODEL_PATH = BASE_DIR / "model" / "house_price_model.pkl"


# Load dataset
data = pd.read_csv(DATASET_PATH)

print("Dataset loaded successfully!")
print(data.head())
print("\nColumns:")
print(data.columns)


# Features
X = data[
    [
        "area",
        "bedrooms",
        "bathrooms",
        "stories",
        "parking"
    ]
]

# Target
y = data["price"]


# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create ML model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


# Train model
model.fit(X_train, y_train)


# Predict test data
predictions = model.predict(X_test)


# Evaluate model
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nModel trained successfully!")
print("Mean Absolute Error:", mae)
print("R2 Score:", r2)


# Save model
joblib.dump(model, MODEL_PATH)

print("\nModel saved successfully at:")
print(MODEL_PATH)