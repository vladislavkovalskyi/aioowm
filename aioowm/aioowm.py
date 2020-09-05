from typing import Optional

import aiohttp

from aioowm.const import const
from aioowm.types.models import Model


class OWM:
	def __init__(self, token: Optional[str], language: Optional[str]):
		"""
		:param token: your api-key https://home.openweathermap.org/api_keys
		:param language: accepts country identifier (en, ru, fr)
		"""
		self.__token = token
		self.language = language

	@staticmethod
	async def get(response: Model):
		return response

	async def weather(self, city: Optional[str]):
		async with aiohttp.ClientSession() as session:
			async with session.get(
					const.request_link.format(
							city=city,
							language=self.language,
							token=self.__token
					)
			) as response:
				return await self.get(response)
