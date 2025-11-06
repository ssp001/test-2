# frontend/app.py
import subprocess
import time
import requests
import streamlit as st

# ------------------ Launch backend ------------------
backend_path = "../backend/server.py"  # adjust relative path
backend_process = subprocess.Popen(
    ["uvicorn", backend_path.replace("\\", "/"), "--host", "127.0.0.1", "--port", "8000"]
)
time.sleep(2)  # wait for backend to start

# ------------------ Streamlit UI ------------------
st.title("ML Prediction App")

param1 = st.slider("Parameter 1", 0.0, 10.0, 1.0)
param2 = st.slider("Parameter 2", 0.0, 10.0, 1.0)
param3 = st.slider("Parameter 3", 0.0, 10.0, 1.0)

if st.button("Predict"):
    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json={"param1": param1, "param2": param2, "param3": param3}
    ).json()
    st.success(f"Prediction: {response['prediction']}")
    if response["warning"]:
        st.warning(response["warning"])
