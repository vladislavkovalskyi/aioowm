# aioowm - Easy Async library for working with OpenWeatherMap

> #### Что нужно, чтобы пользоваться библиотекой:
>#### [PyCharm](https://www.jetbrains.com/ru-ru/pycharm/)
>#### [OpenWeatherMap Token](https://home.openweathermap.org/api_keys)

#### Установка:

```sh
pip install aioowm
pip install -U https://github.com/vladislavkovalskyi/aioowm/archive/master.zip
```

> #### Ссылки:
><a href="https://vk.me/join/AJQ1d5U7ihh63fJPq9y_NWDO">
>    <img src="https://img.shields.io/static/v1?message=VK%20chat&label=&color=orange">
></a>
><a href="https://github.com/vladislavkovalskyi/aioowm/blob/master/docs/docs.md">
>    <img src="https://img.shields.io/static/v1?message=Documentation&label=&color=blue">
></a>

> #### Пример:
>```python
>from asyncio import run
>
>from aioowm import OWM
>
>weather = OWM(token="OpenWeatherMap Token", language="ru")
>
>
>async def app():
>    result = await weather.get("Saint Petersburg")
>    print(
>        f"Город: {result.city.name} ({result.city.country})\n"
>        f"Температура: {result.weather.temperature.now}°C\n"
>        f"Описание: {result.weather.description}\n"
>        f"Скорость ветра: {result.weather.wind.speed} м/с"
>    )
>
>run(app())
>```
>#### Вывод:
>```
>Город: Санкт-Петербург (RU)
>Температура: 2.12°C
>Описание: Облачно
>Скорость ветра: 1.34 м/с
>```