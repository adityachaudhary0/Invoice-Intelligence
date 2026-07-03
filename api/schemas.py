from pydantic import BaseModel, Field


class FreightInput(BaseModel):
    invoice_quantity: float = Field(..., gt=0, description="Invoice quantity", examples=[100])
    invoice_dollars: float = Field(..., ge=0, description="Invoice dollar amount", examples=[5000.0])


class FreightPredictionResponse(BaseModel):
    predicted_freight_cost: float = Field(..., description="Predicted freight cost")
    features_used: dict[str, float] = Field(..., description="Model input features")


class InvoiceInput(BaseModel):
    invoice_quantity: float = Field(..., gt=0, examples=[100])
    invoice_dollars: float = Field(..., ge=0, examples=[5000.0])
    freight: float = Field(..., ge=0, examples=[50.0])
    total_item_quantity: float = Field(..., ge=0, examples=[100])
    total_item_dollars: float = Field(..., ge=0, examples=[5000.0])


class InvoicePredictionResponse(BaseModel):
    flag_invoice: int = Field(..., description="0 = normal, 1 = flagged")
    label: str = Field(..., description="Human-readable prediction label")
    probability: float = Field(..., description="Probability that the invoice is flagged")


class HealthResponse(BaseModel):
    status: str
    models: dict[str, bool]


class ErrorResponse(BaseModel):
    detail: str
