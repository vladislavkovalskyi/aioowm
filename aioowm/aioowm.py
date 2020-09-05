from typing import Optional

import aiohttp

from aioowm.other.const import const


class OWM:
	def __init__(self, token: Optional[str], language: Optional[str]):
		"""
		:param token: your api-key https://home.openweathermap.org/api_keys
		:param language: accepts country identifier (en, ru, fr)
		"""
		self.__token = token
		self.__language = language

	async def get(self, city: Optional[str]):
		self.city = city

		async with aiohttp.ClientSession() as session:
			async with session.get(
					const.request_link.format(
							city=self.city,
							language=self.__language,
							token=self.__token
					)
			) as response:
				return await response.json(encoding='UTF-8')
