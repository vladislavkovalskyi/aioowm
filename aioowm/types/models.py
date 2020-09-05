from pydantic import BaseModel  # ver 1 6 1


class CoordsModel(BaseModel):
	lon: float
	lat: float


class WeatherModel(BaseModel):
	id: int
	main: str
	description: str
	icon: str


class MainModel(BaseModel):
	temp: float
	feels_like: float
	temp_min: float
	temp_max: float
	pressure: int
	humidity: int


class WindModel(BaseModel):
	speed: float
	deg: int


class CloudsModel(BaseModel):
	all: int


class Model(BaseModel):  # Основная модель (главная)
	coords: CoordsModel
	weather: WeatherModel
	base: str
	main: MainModel
	wind: WindModel
	clouds: CoordsModel
	id: int
	name: str

