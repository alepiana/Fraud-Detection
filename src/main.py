from typing import Any

import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel


# Definizione del formato dei dati in ingresso
class Transaction(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    feature4: float


app = FastAPI()

# Carichiamo il modello (il cervello)
MODEL_PATH = "models/fraud_model.joblib"
model = joblib.load(MODEL_PATH)


@app.get("/")
def home() -> dict[str, str]:
    return {"status": "Online", "model_version": "0.1.0"}


@app.post("/predict")
def predict_fraud(data: Transaction) -> dict[str, Any]:
    # Trasformiamo i dati ricevuti in un formato leggibile dal modello (array)
    input_data = np.array(
        [[data.feature1, data.feature2, data.feature3, data.feature4]]
    )

    # Chiediamo al modello: "È una truffa?"
    prediction = model.predict(input_data)

    # Restituiamo il risultato (convertendo da formato numpy a intero Python)
    return {"is_fraud": int(prediction[0]), "probability": "Il modello ha deciso!"}
