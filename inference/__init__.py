from inference.registry import load_models, models_loaded
from inference.freight import predict_freight
from inference.invoice import predict_invoice

__all__ = [
    "load_models",
    "models_loaded",
    "predict_freight",
    "predict_invoice",
]
