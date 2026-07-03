"""Backward-compatible CLI wrapper for freight cost inference."""

import pandas as pd

from inference.freight import predict_freight


def predict_freight_cost(data: dict):
    payload = {
        "Quantity": data["Quantity"],
        "Dollars": data["Dollars"],
    }

    result = predict_freight(payload)
    input_df = pd.DataFrame([data])
    input_df["Predicted_Freight_Cost"] = result["predicted_freight_cost"]
    return input_df


if __name__ == "__main__":
    from inference.registry import load_models

    load_models()

    sample = {"Quantity": 100, "Dollars": 1000}
    print(predict_freight_cost(sample))
