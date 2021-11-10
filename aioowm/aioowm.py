from typing import Optional

from aioowm.const import const
from aioowm.handlers.language import language_handler
from aioowm.handlers.response import response_handler
from aioowm.handlers.temperature import temperature_handler
from aioowm.http.http import request
from aioowm.types.model import Model


class OWM:
    def __init__(
            self,
            token: str,
            language: Optional[str] = "en",
            temperature: Optional[str] = "celsius"
    ):
        """
        :param token: your api-key https://home.openweathermap.org/api_keys
        :param language: accepts country identifier (en, ru, fr)
        :param temperature: accepts temperature (celsius, fahrenheit, kelvin)
        """

        self._token = token
        self.language = language
        self.temperature = temperature

    async def get(self, city: str) -> Model:
        response = await request(
            const.WEATHER_API, {
                "q": city,
                "lang": await language_handler(self.language),
                "units": await temperature_handler(self.temperature),
                "appid": self._token
            }
        )
        response = await response_handler(response)
        return Model(**response)
