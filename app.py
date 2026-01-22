from fastapi import FastAPI, HTTPException
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from model.predict import predict_output, model, MODEL_VERSION
import warnings
warnings.filterwarnings('ignore')

app = FastAPI(title="API for realtime weather prediction", version=MODEL_VERSION)

# ------------------------
# Human-readable endpoint
# ------------------------
@app.get("/")
def home():
    return {"message": "API for realtime weather prediction"}

# ------------------------
# Health check (machine-readable)
# ------------------------
@app.get("/health")
def health_check():
    return {
        "status": "OK",
        "model_loaded": model is not None,
        "model_version": MODEL_VERSION
    }

# ------------------------
# Prediction endpoint
# ------------------------
@app.post("/predict", response_model=PredictionResponse)
def predict(data: UserInput):
    try:
        # Convert Pydantic model to dict for ML model
        model_input = {
            "humidity": data.humidity,
            "wind_speed": data.wind_speed,
            "meanpressure": data.meanpressure,
        }

        prediction_response = predict_output(model_input)

        return prediction_response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
