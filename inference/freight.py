import pandas as pd

from config import FREIGHT_FEATURES
from inference.registry import get_freight_model


def _build_feature_row(data: dict) -> dict:
    quantity = data["Quantity"]
    if quantity == 0:
        raise ValueError("Invoice quantity must be greater than zero.")

    return {
        "Quantity": quantity,
        "Dollars": data["Dollars"],
        "Freight_per_unit": data["Freight"] / quantity,
    }


def predict_freight(data: dict) -> dict:
    model = get_freight_model()
    features = _build_feature_row(data)
    input_df = pd.DataFrame([features])[FREIGHT_FEATURES]

    predicted_cost = float(model.predict(input_df)[0])

    return {
        "predicted_freight_cost": round(predicted_cost, 2),
        "features_used": features,
    }
