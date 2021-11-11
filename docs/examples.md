### Пример работы с error:

```python
...

async def app():
    result = await weather.get(input("Введите город: "))
    if not result.error:
        print("Запрос обработан успешно, поэтому можно получать информацию о погоде!")
    else:
        print("Запрос обработан с ошибкой, возможно вы ввели неизвестный город!")

...
```

### Пример работы с code:

```python
...

async def app():
    result = await weather.get(input("Введите город: "))
    if result.code == 200:
        print("Запрос обработан успешно, поэтому можно получать информацию о погоде!")
    else:
        print(f"Запрос обработан с ошибкой: {result.code}")

...
```

### Пример работы с default:

```python
...

async def app():
    result = await weather.get(input("Введите город: "))
    print(
        f"Погода в городе: {result['name']}\n"
        f"Температура: {result['main']['temp']}°C\n"
        f"Скорость ветра: {result['wind']['speed']} м/с"
    )

...
```

### Пример работы с city:

```python

...

async def app():
    result = await weather.get(input("Введите город: "))
    print(
        f"Айди города: {result.city.id}\n"
        f"Название города: {result.city.name}\n"
        f"Страна, в которой город: {result.city.country}\n"
        f"Временная зона: {result.city.timezone}\n"
        f"Рассвет (UNIX): {result.city.sunrise}\n"
        f"Закат (UNIX): {result.city.sunset}\n"
        f"Координаты города: long: {result.city.coordinates.longitude}, lat: {result.city.coordinates.latitude}"
    )

...

```

### Пример работы с weather:

```python

...


async def app():
    result = await weather.get(input("Введите город: "))
    print(
        f"Описание (голое): {result.weather.main}\n"
        f"Описание: {result.weather.description}\n"
        f"Облачность: {result.weather.clouds}%\n"
        f"Дождь: {result.weather.rain} см\n"
        f"Снег: {result.weather.snow} см\n"
        f"Влажность: {result.weather.humidity}%\n"
        f"Давление: {result.weather.pressure.value}\n"
        f"Давление (на уровне земли): {result.weather.pressure.ground_level}\n"
        f"Давление (на уровне моря): {result.weather.pressure.sea_level}\n"
        f"Ветер (скорость): {result.weather.wind.speed} м/с\n"
        f"Ветер (направление в градусах): {result.weather.wind.direction}\n"
        f"Ветер (порыв): {result.weather.wind.gust} м/с\n"
        f"Температура (в данный момент): {result.weather.temperature.now}°C\n"
        f"Температура (минимальная): {result.weather.temperature.minimal}°C\n"
        f"Температура (максимальная): {result.weather.temperature.maximal}°C\n"
        f"Температура (по ощущениям человека): {result.weather.temperature.feels_like}°C"
    )


loop = asyncio.get_event_loop()
loop.run_until_complete(app())

...

```