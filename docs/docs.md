## OWM

### `OWM()` - Инициализация класса.

> Принимает аргументы:
>
> `token` - токен пользователя **([брать отсюда](https://home.openweathermap.org/api_keys))**
>
> `language` - язык **(код страны, язык которой вы хотите использовать)**
>
> `temperature` - единицы измерения температуры **(celsius, fahrenheit, kelvin)**

#

### `.get()` - Получение информации о погоде.

> Принимает аргумент `city`, который может состоять из **латиницы** или **кириллицы**
>
>Возвращает [**response**](methods.md) (который можно записать в вашу переменную и в дальнейшем с ней работать. *см. пример*)

### [Здесь](methods.md) вы можете узнать, какие методы есть в [**response**](methods.md) и как работать с ними

### Пример:

```python
import asyncio

from aioowm import OWM

weather = OWM("token", "ru", "celsius")


async def app():
    result = await weather.get(input("Введите город: "))
    print(
        f"Город: {result.city.name} ({result.city.country})\n"
        f"Температура: {result.weather.temperature.now}°C\n"
        f"Описание: {result.weather.description}\n"
        f"Скорость ветра: {result.weather.wind.speed} м/с"
    )


loop = asyncio.get_event_loop()
loop.run_until_complete(app())
```