import joblib
import pandas as pd
from schema.prediction_response import PredictionResponse

MODEL_VERSION = "1.0.0"

model = joblib.load("model/model.joblib")

FEATURE_COLUMNS = ["humidity", "wind_speed", "meanpressure"]

def predict_output(input_data: dict) -> PredictionResponse:
    X = pd.DataFrame([input_data], columns=FEATURE_COLUMNS)

    #numeric prediction
    prediction = float(model.predict(X)[0])
    
    return PredictionResponse(
        predicted_value=prediction, m_version_name=MODEL_VERSION)