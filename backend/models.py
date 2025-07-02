from pydantic import BaseModel

class UserRegister(BaseModel):
    email: str; password: str

class UserLogin(BaseModel):
    email: str; password: str

class Preferences(BaseModel):
    price_threshold: float
    preferred_time: str
    vehicle_range: int
