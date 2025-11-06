#%%
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from typing import Union,Literal,Annotated
from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel,Field
from pipeline.train_evaluation_data import Training_Evaluation
from sklearn.preprocessing import OrdinalEncoder
import numpy as np

# %%
class User_parameter(BaseModel):
    
   Age  :Annotated[int,Field(gt=0,description="What is your current Age ")]
   Gender:Literal["Male","Female"] = Field(Literal,description="There is you can assine your gender")
   Blood_Group: Annotated[Literal["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],Field(description="There you have to assine your Blood group")] 
   WBC_Count_int :Annotated[int,Field(int,description="WBC count")]
   RBC_Count_float :Annotated[float,Field(float,description="RBC count")]
   Hematocrit_float :Annotated[float,Field(float,description="Hemotocrit")]
   Hemoglobin_float :Annotated[float,Field(float,description="Hemoglobin")]
   Platelet_Count_int :Annotated[int,Field(int,description="Platelet count")]
   MCV_float :Annotated[float,Field(float,description="MCV")]
   MCH_float :Annotated[float,Field(float,description="MCH")]
   MCHC_float :Annotated[float,Field(float,description="MCHC")]
   LDH_Level_float :Annotated[float,Field(float,description="LDH Level")]
   Serum_Calcium_float:Annotated[float,Field(float,description="Serum Calcium")]
   Total_Protein_float:Annotated[float,Field(float|int,description="Total Protine")]
   Albumin_float:Annotated[float,Field(float,description="Albumin")]
   ESR_int :Annotated[int,Field(int,description="ESR")]
   Fatigue:Annotated[Literal["yes","no"],Field(Literal,description="Fatigue")]
   Weight_Loss:Annotated[Literal["yes","no"],Field(Literal,description="Weight Loss")]
   Bone_Pain:Annotated[Literal["yes","no"],Field(Literal,description="Bone pain")]
   Fever:Annotated[Literal["yes","no"],Field(Literal,description="Fever")]
   Night_Sweats:Annotated[Literal["yes","no"],Field(Literal,description="Night Sweat")]
   Enlarged_Lymph_Nodes:Annotated[Literal["yes","no"],Field(Literal,description="Enlarged Lymphed Node")]
   Smoking_Habit:Annotated[Literal["yes","no"],Field(Literal,description="Smoking Habit")]
   Alcohol_Consumption :Annotated[Literal["yes","no"],Field(Literal,description="Alocohol Consumtion")] 
   Physical_Activity:Annotated[Literal["Moderate", "Sedentary", "Active"],Field(Literal,description="Physical Activity,Options are Moderate,Sedentary,Activity")]
   Family_Cancer_History:Annotated[Literal["yes","no"],Field(Literal,description="Family Cancer History")]
   Previous_Blood_Disorde:Annotated[Literal['yes','no'],Field(Literal,description="Previous_Blood_Disorde")]


# %%
app = FastAPI(title="Blood cancer prediction model",version="0.0.1", description="An API that predicts Blood Cancer Diagnosis and Disease Stage based on 21 medical input parameters.")
# %%




#%%

@app.get("/")
def Home_router():
   return {"hello world This is the home page of the backeend server 💩🥸"}
   

@app.post("/predict")
def predict_digonasis(user_parameter:User_parameter):

   Age = user_parameter.Age
   Gender = user_parameter.Gender
   Blood_Group = user_parameter.Blood_Group
   WBC_Count = user_parameter.WBC_Count_int
   RBC_Count = user_parameter.RBC_Count_float
   Hematocrit_float = user_parameter.Hematocrit_float
   Hemoglobin = user_parameter.Hemoglobin_float
   Platelet_Count = user_parameter.Platelet_Count_int
   MCV = user_parameter.MCV_float
   MCH = user_parameter.MCH_float
   MCHC = user_parameter.MCHC_float
   LDH_Level = user_parameter.LDH_Level_float
   Serum_Calcium = user_parameter.Serum_Calcium_float
   Total_Protein = user_parameter.Total_Protein_float
   Albumin = user_parameter.Albumin_float
   ESR = user_parameter.ESR_int
   Fatigue = user_parameter.Fatigue
   Weight_Loss = user_parameter.Weight_Loss
   Bone_Pain = user_parameter.Bone_Pain
   Fever = user_parameter.Fever
   Night_Sweats = user_parameter.Night_Sweats
   Enlarged_Lymph_Nodes = user_parameter.Enlarged_Lymph_Nodes
   Smoking_Habit = user_parameter.Smoking_Habit
   Alcohol_Consumption = user_parameter.Alcohol_Consumption
   Physical_Activity = user_parameter.Physical_Activity
   Family_Cancer_History = user_parameter.Family_Cancer_History
   Previous_Blood_Disorde = user_parameter.Previous_Blood_Disorde
   
   data = [[ Age, Gender, Blood_Group, WBC_Count, RBC_Count, Hematocrit_float, Hemoglobin,
    Platelet_Count, MCV, MCH, MCHC, LDH_Level, Serum_Calcium, Total_Protein,
    Albumin, ESR, Fatigue, Weight_Loss, Bone_Pain, Fever, Night_Sweats,
    Enlarged_Lymph_Nodes, Smoking_Habit, Alcohol_Consumption,
    Physical_Activity, Family_Cancer_History, Previous_Blood_Disorde]]
   
   df = pd.DataFrame(data, columns=[
        'Age', 'Gender', "Blood_Group", "WBC_Count", "RBC_Count",
        'Hematocrit', 'Hemoglobin', 'Platelet_Count', 'MCV', 'MCH', "MCHC",
        "LDH_Level", "Serum_Calcium", "Total_Protein", "Albumin", "ESR",
        "Fatigue", "Weight_Loss", "Bone_Pain", "Fever", "Night_Sweats",
        "Enlarged_Lymph_Nodes", "Smoking_Habit", "Alcohol_Consumption",
        "Physical_Activity", "Family_Cancer_History", "Previous_Blood_Disorde"
    ])
  
   oe = OrdinalEncoder()
   categories=[  'Gender', 'Blood_Group', 'Fatigue', 'Weight_Loss', 'Bone_Pain',
        'Fever', 'Night_Sweats', 'Enlarged_Lymph_Nodes', 'Smoking_Habit',
        'Alcohol_Consumption', 'Physical_Activity', 'Family_Cancer_History',
        'Previous_Blood_Disorde']
   for col in categories:
    df[col] = df[col].astype(str).str.strip().str.lower().map({
        "yes": 1,
        "no": 0
    }).fillna(0)  

   featurs_dict = df.to_dict(orient='records')[0]
   
   trainer = Training_Evaluation() 
   
   result = trainer.model_predict(featurs_dict)
   
   return {"prediction": result}
   
# %%

