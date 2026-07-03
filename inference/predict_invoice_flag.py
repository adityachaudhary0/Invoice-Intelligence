"""Backward-compatible CLI wrapper for invoice flagging inference."""

from inference.invoice import predict_invoice


def predict_invoice_flag(data: dict):
    result = predict_invoice(data)
    data = data.copy()
    data["Predicted_Invoice_Flag"] = result["flag_invoice"]
    return data


if __name__ == "__main__":
    from inference.registry import load_models

    load_models()

    sample = {
        "Invoice_Quantity": 100,
        "Invoice_Dollars": 1000,
        "Freight": 100,
        "Total_Item_Quantity": 100,
        "Total_Item_Dollars": 1000,
    }
    print(predict_invoice_flag(sample))
