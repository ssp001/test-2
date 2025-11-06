# app_full.py
import os
import threading
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from keras.models import load_model
import streamlit as st
import time

# ----------------------
# Backend API (FastAPI)
# ----------------------
app = FastAPI()

# Example input schema
class InputData(BaseModel):
    param1: float
    param2: float
    param3: float

# Load Model
model_path = os.path.join("pipeline", "model_disk", "Blood_cancer_prediction_model.h5")
if not os.path.exists(model_path):
    print(f"Model not found at {model_path}. Please save your trained model first!")
    model = None
else:
    model = load_model(model_path)

@app.post("/predict")
def predict(data: InputData):
    if model is None:
        return {"error": "Model not loaded."}
    
    features = np.array([[data.param1, data.param2, data.param3]])
    prediction = model.predict(features)
    confidence = float(np.max(prediction))
    result = {
        "prediction": prediction.tolist(),
        "confidence": confidence
    }
    if confidence < 0.5:
        result["warning"] = "Prediction confidence is low. Result may be unreliable!"
    return result

# ----------------------
# Streamlit Frontend
# ----------------------
def run_streamlit():
    st.title("Blood Cancer Prediction App")

    # Sliders for input
    param1 = st.slider("Parameter 1", 0, 100)
    param2 = st.slider("Parameter 2", 0, 100)
    param3 = st.slider("Parameter 3", 0, 100)

    if st.button("Predict"):
        if model is None:
            st.warning("Model not loaded. Prediction not possible!")
        else:
            features = np.array([[param1, param2, param3]])
            prediction = model.predict(features)
            confidence = np.max(prediction)
            st.success(f"Prediction: {prediction}")
            if confidence < 0.5:
                st.warning("Prediction confidence is low. Result may be unreliable!")

# ----------------------
# Run both servers
# ----------------------
def run_backend():
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    # Run FastAPI in a separate thread
    threading.Thread(target=run_backend, daemon=True).start()

    # Small delay to allow FastAPI server to start
    time.sleep(1)

    # Run Streamlit frontend
    run_streamlit()
