from fastapi import APIRouter, HTTPException

from api.schemas import FreightInput, FreightPredictionResponse
from inference.freight import predict_freight

router = APIRouter(prefix="/predict", tags=["Freight Cost Prediction"])


@router.post(
    "/freight",
    response_model=FreightPredictionResponse,
    summary="Predict expected freight cost",
    responses={
        400: {"description": "Invalid input"},
        500: {"description": "Prediction failed"},
    },
)
def predict_freight_cost(payload: FreightInput) -> FreightPredictionResponse:
    try:
        result = predict_freight(
            {
                "Quantity": payload.invoice_quantity,
                "Dollars": payload.invoice_dollars,
            }
        )
        return FreightPredictionResponse(**result)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Freight prediction failed.") from exc
