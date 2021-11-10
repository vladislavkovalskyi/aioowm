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
