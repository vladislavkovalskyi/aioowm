from typing import Optional

from aioowm.const import const
from aioowm.http.http import request
from aioowm.types.models import Model


class OWM:
	def __init__(self, token: str, language: Optional[str]):
		"""
		:param token: your api-key https://home.openweathermap.org/api_keys
		:param language: accepts country identifier (en, ru, fr)
		"""
		self._token = token
		self.language = language

	async def get(self, city: str) -> Model:
		response = await request(
				const.weather_api, {
					'q':     city,
					'lang':  self.language,
					'appid': self._token
				}
		)
		return Model(**response)
