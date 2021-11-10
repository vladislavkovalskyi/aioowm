## Методы response

### Мы уже знаем, что `.get()` возвращает **response**. Давайте рассмотрим, как работать с этим:

```python
...


async def app():
    result = await weather.get(input("Введите город: "))
    print(
        f"Город: {result.city.name} ({result.city.country})\n"
        f"Температура: {result.weather.temperature.now}°C\n"
        f"Описание: {result.weather.description}\n"
        f"Скорость ветра: {result.weather.wind.speed} м/с"
    )


...
```

[Полный код](docs.md) в примерах.

### Основные методы **response** (примеры использования [здесь](examples.md)):

> `error` - возвращает **True** или **False** (**bool**), в зависимости от того, получилось ли обработать запрос.
>
> `code` - возвращает **int** коды об выполнение запроса (200 - успешно, про остальные коды вы можете прочитать в
> документации [**OpenWeatherMap**](https://openweathermap.org/current))
>
> `default` - возвращает чистый, не отформатированный **dict**, который расписан в
> [примерах](https://openweathermap.org/current#current_JSON) на **OpenWeatherMap**
> 
> `city` - возвращает всю информацию о модели города (*CityModel*):
>
> `weather` - возвращает всю информацию о модели погода (*WeatherModel*)