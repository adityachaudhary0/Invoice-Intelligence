from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

INVOICE_MODEL_PATH = PROJECT_ROOT / "invoice_flagging" / "models" / "predict_flag_invoice.pkl"
INVOICE_SCALER_PATH = PROJECT_ROOT / "invoice_flagging" / "models" / "scaler.pkl"
FREIGHT_MODEL_PATH = PROJECT_ROOT / "freight_cost_prediction" / "models" / "predict freight_model.pkl"

INVOICE_FEATURES = [
    "Invoice_Quantity",
    "Invoice_Dollars",
    "Freight",
    "Total_Item_Quantity",
    "Total_Item_Dollars",
]

FREIGHT_FEATURES = ["Quantity", "Dollars"]
