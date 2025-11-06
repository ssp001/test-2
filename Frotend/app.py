import streamlit as st
import numpy as np
import tensorflow as tf
from keras.models import load_model

# --- Load model ---
import os
import os
from keras.models import load_model
# Base directory
base_dir = r"C:\Users\shova\Desktop\project\test-2"

# Join paths
model_path = os.path.join(base_dir, "pipeline", "model_disk", "Blood_cancer_prediction_model.h5")

# Load the model
model = load_model(model_path)
print("Model loaded successfully!")

# --- Labels (replace with your real labels) ---
diag_labels = ['Leukemia', 'Lymphoma', 'Myeloma', 'Normal']
stage_labels = ['Stage I', 'Stage II', 'Stage III', 'Stage IV', 'Stage V', 'Negative']

st.title("🩸 Blood Cancer Prediction App")

st.markdown("Adjust the parameters and click **Predict** to see the diagnosis and disease stage.")

# --- User inputs in columns ---
col1, col2, col3 = st.columns(3)

with col1:
    age = st.slider("Age", 0, 100, 25)
    gender = st.selectbox("Gender", ["Male", "Female"])
    blood_group = st.selectbox("Blood Group", ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"])
    wbc_count = st.number_input("WBC Count (cells/µL)", 0, 1000000, 50000)
    rbc_count = st.number_input("RBC Count (million/µL)", 0.0, 10.0, 4.5)
    hemoglobin = st.number_input("Hemoglobin (g/dL)", 0.0, 20.0, 12.0)

with col2:
    hematocrit = st.number_input("Hematocrit (%)", 0.0, 60.0, 35.0)
    platelet_count = st.number_input("Platelet Count (cells/µL)", 0, 1000000, 250000)
    mcv = st.number_input("MCV (fL)", 0.0, 150.0, 90.0)
    mch = st.number_input("MCH (pg)", 0.0, 50.0, 30.0)
    mchc = st.number_input("MCHC (g/dL)", 0.0, 40.0, 34.0)
    ldh_level = st.number_input("LDH Level (U/L)", 0.0, 5000.0, 250.0)

with col3:
    serum_calcium = st.number_input("Serum Calcium (mg/dL)", 0.0, 20.0, 9.5)
    total_protein = st.number_input("Total Protein (g/dL)", 0.0, 15.0, 7.0)
    albumin = st.number_input("Albumin (g/dL)", 0.0, 10.0, 4.0)
    esr = st.number_input("ESR (mm/hr)", 0, 200, 20)
    fatigue = st.selectbox("Fatigue", ["Yes", "No"])
    weight_loss = st.selectbox("Weight Loss", ["Yes", "No"])
    bone_pain = st.selectbox("Bone Pain", ["Yes", "No"])
    fever = st.selectbox("Fever", ["Yes", "No"])
    night_sweats = st.selectbox("Night Sweats", ["Yes", "No"])
    enlarged_lymph_nodes = st.selectbox("Enlarged Lymph Nodes: (a common sign that the body is fighting an infection)", ["Yes", "No"])
    smoking_habit = st.selectbox("Smoking Habit", ["Yes", "No"])
    alcohol_consumption = st.selectbox("Alcohol Consumption", ["Yes", "No"])
    physical_activity = st.selectbox("Physical Activity", ["Sedentary", "Moderate", "Active"])
    family_cancer_history = st.selectbox("Family Cancer History", ["Yes", "No"])
    previous_blood_disorder = st.selectbox("Previous Blood Disorder", ["Yes", "No"])

# --- Convert categorical inputs ---
gender = 1 if gender == "Male" else 0
blood_group_dict = {"O+":0,"O-":1,"A+":2,"A-":3,"B+":4,"B-":5,"AB+":6,"AB-":7}
blood_group = blood_group_dict[blood_group]
fatigue = 1 if fatigue=="Yes" else 0
weight_loss = 1 if weight_loss=="Yes" else 0
bone_pain = 1 if bone_pain=="Yes" else 0
fever = 1 if fever=="Yes" else 0
night_sweats = 1 if night_sweats=="Yes" else 0
enlarged_lymph_nodes = 1 if enlarged_lymph_nodes=="Yes" else 0
smoking_habit = 1 if smoking_habit=="Yes" else 0
alcohol_consumption = 1 if alcohol_consumption=="Yes" else 0
physical_activity_dict = {"Sedentary":0, "Moderate":1, "Active":2}
physical_activity = physical_activity_dict[physical_activity]
family_cancer_history = 1 if family_cancer_history=="Yes" else 0
previous_blood_disorder = 1 if previous_blood_disorder=="Yes" else 0

# --- Predict button ---
if st.button("Predict"):
    # --- Prepare input ---
    input_data = np.array([[age, gender, blood_group, wbc_count, rbc_count, hemoglobin,
                            hematocrit, platelet_count, mcv, mch, mchc, ldh_level,
                            serum_calcium, total_protein, albumin, esr,
                            fatigue, weight_loss, bone_pain, fever, night_sweats,
                            enlarged_lymph_nodes, smoking_habit, alcohol_consumption,
                            physical_activity, family_cancer_history, previous_blood_disorder]])

    # --- Predict ---
    diag_pred, stage_pred = model.predict(input_data)

    # Get class indices
    diag_idx = np.argmax(diag_pred)
    stage_idx = np.argmax(stage_pred)

    # --- Display results ---
    st.subheader("🧪 Diagnosis Prediction")
    st.write(f"**Predicted Diagnosis:** {diag_labels[diag_idx]}")
    st.bar_chart(diag_pred[0])

    st.subheader("📊 Disease Stage Prediction")
    st.write(f"**Predicted Stage:** {stage_labels[stage_idx]}")
    st.warning("Prediction confidence is low. Result may be unreliable!")
    st.bar_chart(stage_pred[0])
