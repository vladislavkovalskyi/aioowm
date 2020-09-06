# aioowm - Easy Async library for working with OpenWeatherMap

#### Installing (Установка):
```sh
pip install -U https://github.com/vladislavkovalskyi/aioowm/archive/master.zip
```

#### Links (Ссылки):
<a href="https://vk.me/join/AJQ1d5U7ihh63fJPq9y_NWDO">
    <img src="https://img.shields.io/static/v1?message=Chat%20VKontakte&label=&color=orange">
    
</a>

#### Example (Пример):
```python
from aioowm import OWM
import asyncio


weather = OWM(token='Token Here', language='ru')
# https://home.openweathermap.org/api_keys
# language accepts country identifier (en, ru, fr)

async def app():
    result = await weather.get(city='Moscow')
    print(result.name)  # City name
    print(result.coord.lat, result.coord.lon)  # Coords of your city

    print(result)

asyncio.run(app())
```