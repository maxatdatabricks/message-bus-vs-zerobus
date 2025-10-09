from pydantic import BaseModel
from datetime import datetime

class AirQuality(BaseModel):
    device_name: str
    temp: int
    humidity: int
    source: str
    timestamp: datetime