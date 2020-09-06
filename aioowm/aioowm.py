from typing import Optional

import aiohttp

from aioowm.const import const
from aioowm.http.http import request
from aioowm.types.models import Model


class OWM:
	def __init__(self, token: Optional[str], language: Optional[str]):
		"""
		:param token: your api-key https://home.openweathermap.org/api_keys
		:param language: accepts country identifier (en, ru, fr)
		"""
		self.__token = token
		self.language = language

	async def get(self, city: Optional[str]) -> Model:
		response = await request(const.request_link.format(
							city=city,
							language=self.language,
							token=self.__token)
		)

		return Model(**response)
