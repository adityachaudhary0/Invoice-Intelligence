from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api.routes import freight, invoice
from api.schemas import HealthResponse
from inference.registry import load_models, models_loaded


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_models()
    yield


app = FastAPI(
    title="AI Powered Invoice Intelligence System",
    description=(
        "Production-ready API for freight cost prediction and invoice risk flagging. "
        "Models are loaded once at startup and reused for all inference requests."
    ),
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(freight.router)
app.include_router(invoice.router)


@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(status_code=400, content={"detail": str(exc)})


@app.get("/", tags=["System"])
def home():
    return {
        "message": "AI Powered Invoice Intelligence System API",
        "docs": "/docs",
        "endpoints": {
            "freight_prediction": "POST /predict/freight",
            "invoice_prediction": "POST /predict/invoice",
            "health": "GET /health",
        },
    }


@app.get("/health", response_model=HealthResponse, tags=["System"])
def health():
    loaded = models_loaded()
    all_loaded = all(loaded.values())
    return HealthResponse(
        status="ok" if all_loaded else "degraded",
        models=loaded,
    )
