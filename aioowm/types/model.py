from typing import Optional

from pydantic import BaseModel

from aioowm.types.city import CityModel
from aioowm.types.weather import WeatherModel


class Model(BaseModel):
    error: Optional[bool] = None
    code: Optional[int] = None
    default: Optional[dict] = None
    city: Optional[CityModel] = None
    weather: Optional[WeatherModel] = None


