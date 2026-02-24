from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load model
model = joblib.load("model.joblib")

app = FastAPI()

class InputData(BaseModel):
    features: list[float]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: InputData):
    X = [data.features]
    pred = model.predict(X)[0]
    return {"prediction": int(pred)}
