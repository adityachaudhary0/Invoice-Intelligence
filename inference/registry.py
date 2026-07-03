import joblib

from config import (
    FREIGHT_MODEL_PATH,
    INVOICE_MODEL_PATH,
    INVOICE_SCALER_PATH,
)

_invoice_model = None
_invoice_scaler = None
_freight_model = None


def load_models() -> None:
    global _invoice_model, _invoice_scaler, _freight_model

    if not INVOICE_MODEL_PATH.exists():
        raise FileNotFoundError(f"Invoice model not found: {INVOICE_MODEL_PATH}")
    if not INVOICE_SCALER_PATH.exists():
        raise FileNotFoundError(f"Invoice scaler not found: {INVOICE_SCALER_PATH}")
    if not FREIGHT_MODEL_PATH.exists():
        raise FileNotFoundError(f"Freight model not found: {FREIGHT_MODEL_PATH}")

    _invoice_model = joblib.load(INVOICE_MODEL_PATH)
    _invoice_scaler = joblib.load(INVOICE_SCALER_PATH)
    _freight_model = joblib.load(FREIGHT_MODEL_PATH)


def models_loaded() -> dict[str, bool]:
    return {
        "invoice_model": _invoice_model is not None,
        "invoice_scaler": _invoice_scaler is not None,
        "freight_model": _freight_model is not None,
    }


def get_invoice_model():
    if _invoice_model is None or _invoice_scaler is None:
        raise RuntimeError("Models not loaded. Call load_models() during application startup.")
    return _invoice_model, _invoice_scaler


def get_freight_model():
    if _freight_model is None:
        raise RuntimeError("Models not loaded. Call load_models() during application startup.")
    return _freight_model
