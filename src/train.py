import os

import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier


def train() -> None:
    # Generazione dati sintetici
    X = np.random.rand(1000, 4)
    y = (X[:, 0] * X[:, 2] > 0.7).astype(int)

    model = RandomForestClassifier()
    model.fit(X, y)

    # Path corretto: sale di un livello e entra in models
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/fraud_model.joblib")
    print("✅ Modello salvato in models/fraud_model.joblib")


if __name__ == "__main__":
    train()
