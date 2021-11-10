from typing import Optional


async def temperature_handler(temperature: Optional[str]) -> str:
    """
    :param temperature: accepts temp identifier (celsius, fahrenheit, kelvin)
    :return: units
    """
    identifiers = {"celsius": "metric", "fahrenheit": "imperial", "kelvin": "kelvin"}

    if temperature.lower() not in identifiers:
        raise TypeError("Unknown temperature identifier!")
    else:
        return identifiers[temperature]