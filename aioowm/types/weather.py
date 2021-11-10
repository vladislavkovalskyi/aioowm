from typing import Optional

from pydantic import BaseModel


class PressureModel(BaseModel):
    sea_level: Optional[int] = None
    ground_level: Optional[int] = None
    value: Optional[int] = None


class WindModel(BaseModel):
    speed: Optional[float] = None
    direction: Optional[int] = None
    gust: Optional[float] = None


class TemperatureModel(BaseModel):
    now: Optional[float] = None
    minimal: Optional[float] = None
    maximal: Optional[float] = None
    feels_like: Optional[float] = None


class WeatherModel(BaseModel):
    id: Optional[int] = None
    main: Optional[str] = None
    description: Optional[str] = None
    clouds: Optional[int] = None
    rain: Optional[float] = None
    snow: Optional[float] = None
    humidity: Optional[int] = None
    pressure: Optional[PressureModel] = None
    wind: Optional[WindModel] = None
    temperature: Optional[TemperatureModel] = None
