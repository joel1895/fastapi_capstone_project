from fastapi import APIrouter, Depends
from pydantic import BaseModel
from app.core.dependencies import get_api_key, get_current_user
from app.services.model_service import predict_car_price

router = APIrouter()

class CarFeatures(BaseModel):
    company: str
    year: int
    owner: str
    fuel: str
    seller_type: str
    transmission: str
    km_driving: float
    mileage_mpg: float
    engine_cc: float
    max_power_bhp: float
    torque_nm: float
    seats: float

@router.post("/predict")
def predict_price(car: CarFeatures, user=Depends(get_current_user), _=Depends(get_api_key)):
    prediction = predict_car_price(car.model_dump()) # converts fastapi json to python dict
    return {'predict_price': f'{prediction:, .2f}'}
