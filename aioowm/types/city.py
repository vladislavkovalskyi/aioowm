from typing import Optional

from pydantic import BaseModel


class CoordinatesModel(BaseModel):
    longitude: Optional[float] = None
    latitude: Optional[float] = None


class CityModel(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    country: Optional[str] = None
    timezone: Optional[int] = None
    sunrise: Optional[int] = None
    sunset: Optional[int] = None
    coordinates: Optional[CoordinatesModel] = None
