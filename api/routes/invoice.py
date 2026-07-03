from fastapi import APIRouter, HTTPException

from api.schemas import InvoiceInput, InvoicePredictionResponse
from inference.invoice import predict_invoice

router = APIRouter(prefix="/predict", tags=["Invoice Risk Prediction"])


@router.post(
    "/invoice",
    response_model=InvoicePredictionResponse,
    summary="Predict invoice risk flag",
    responses={
        400: {"description": "Invalid input"},
        500: {"description": "Prediction failed"},
    },
)
def predict_invoice_flag(payload: InvoiceInput) -> InvoicePredictionResponse:
    try:
        result = predict_invoice(
            {
                "Invoice_Quantity": payload.invoice_quantity,
                "Invoice_Dollars": payload.invoice_dollars,
                "Freight": payload.freight,
                "Total_Item_Quantity": payload.total_item_quantity,
                "Total_Item_Dollars": payload.total_item_dollars,
            }
        )
        return InvoicePredictionResponse(**result)
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Invoice prediction failed.") from exc
