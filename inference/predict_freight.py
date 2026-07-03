"""Backward-compatible CLI wrapper for freight cost inference."""

import pandas as pd

from inference.freight import predict_freight


def predict_freight_cost(data: dict):
    if "Freight_per_unit" not in data:
        payload = {
            "Quantity": data["Quantity"],
            "Dollars": data["Dollars"],
            "Freight": data.get("Freight", data["Quantity"] * data["Freight_per_unit"]),
        }
    else:
        payload = {
            "Quantity": data["Quantity"],
            "Dollars": data["Dollars"],
            "Freight": data["Quantity"] * data["Freight_per_unit"],
        }

    result = predict_freight(payload)
    input_df = pd.DataFrame([data])
    input_df["Predicted_Freight_Cost"] = result["predicted_freight_cost"]
    return input_df


if __name__ == "__main__":
    from inference.registry import load_models

    load_models()

    sample = {"Quantity": 100, "Dollars": 1000, "Freight_per_unit": 10}
    print(predict_freight_cost(sample))
