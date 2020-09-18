from pydantic import BaseModel

from typing import List


class CoordModel(BaseModel):
	lon: float = None
	lat: float = None


class WeatherModel(BaseModel):
	id: int = None
	main: str = None
	description: str = None
	icon: str = None


class MainModel(BaseModel):
	temp: float = None
	feels_like: float = None
	temp_min: float = None
	temp_max: float = None
	pressure: int = None
	humidity: int = None


class WindModel(BaseModel):
	speed: float = None
	deg: int = None


class CloudsModel(BaseModel):
	all: int = None


class SysModel(BaseModel):
	type: int = None
	id: int = None
	country: str = None
	sunrise: int = None
	sunset: int = None


class Model(BaseModel):
	coord: CoordModel = None
	weather: List[WeatherModel] = None
	base: str = None
	main: MainModel = None
	visibility: int = None
	wind: WindModel = None
	clouds: CloudsModel = None
	dt: int = None
	sys: SysModel = None
	timezone: int = None
	id: int = None
	name: str = None
	cod: int = None
	message: str = None
