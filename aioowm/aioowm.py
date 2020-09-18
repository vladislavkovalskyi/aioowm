from typing import Optional

from aioowm.const import const
from aioowm.http.http import request
from aioowm.types.models import Model
from aioowm.handlers.handlers import language, temperature


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
				const.weather_api, {
					"q": city,
					"lang": await language(self.language),
					"units": await temperature(self.temperature),
					"appid": self._token
				}
		)
		return Model(**response)
