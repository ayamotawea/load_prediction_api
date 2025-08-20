#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load your model
model = joblib.load("load_model.pkl")

# Input schema
class LoadInput(BaseModel):
    X1: float
    X2: float
    X3: float
    X4: float
    X5: float
    X6: float
    X7: float
    X8: float

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Load Prediction API is working!"}

@app.post("/predict")
def predict(data: LoadInput):
    input_data = [[
        data.X1, data.X2, data.X3, data.X4,
        data.X5, data.X6, data.X7, data.X8
    ]]
    prediction = model.predict(input_data)
    # Assuming model.predict returns [[Y1, Y2]]
    return {"Y1": float(prediction[0][0]), "Y2": float(prediction[0][1])}

