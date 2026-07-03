import pandas as pd

from config import INVOICE_FEATURES
from inference.registry import get_invoice_model


def predict_invoice(data: dict) -> dict:
    model, scaler = get_invoice_model()

    input_df = pd.DataFrame([data])[INVOICE_FEATURES]
    scaled_features = scaler.transform(input_df)

    prediction = int(model.predict(scaled_features)[0])
    probability = float(model.predict_proba(scaled_features)[0][1])

    return {
        "flag_invoice": prediction,
        "label": "Flagged Invoice" if prediction == 1 else "Normal Invoice",
        "probability": round(probability, 4),
    }
