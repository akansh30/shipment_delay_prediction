import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI app
app = FastAPI()

# Load the Logistic Regression model
logistic_regression_model = joblib.load("models/logistic_regression_model.pkl")

# Define the input data model using Pydantic for validation
class ShipmentDetails(BaseModel):
    distance: float
    delivery_duration: float
    planned_vs_actual_delay: float

# Preprocessing function to format input data
def preprocess_input(data):
    # Correct column names to match what the model expects
    processed_data = {
        'Distance (km)': data['distance'],
        'Delivery Duration': data['delivery_duration'],
        'Planned vs Actual Delay': data['planned_vs_actual_delay']
    }
    return pd.DataFrame([processed_data])

@app.post("/predict/")
async def predict(shipment: ShipmentDetails):
    # Preprocess input data from request
    input_data = preprocess_input(shipment.dict())

    # Make prediction using Logistic Regression model
    log_reg_prediction = logistic_regression_model.predict(input_data)

    # Return prediction
    return {
        "log_reg_prediction": "Delayed" if log_reg_prediction[0] == 1 else "On Time"
    }

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Shipment Prediction API"}
