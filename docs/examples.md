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

###City и Weather скоро допишутся.