from pydantic import BaseModel, Field
from datetime import date

class UserInput(BaseModel):
    humidity: float = Field(..., ge=0, le=100)
    wind_speed: float = Field(..., ge=0, le=50)
    meanpressure: float = Field(..., ge=0, le=2000)
   