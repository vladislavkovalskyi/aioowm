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

	@property
	async def token(self):
		return self.__token

	@token.setter
	async def token(self, token: Optional[str]):
		self.__token = token

	@property
	async def language(self):
		return self.__language

	@language.setter
	async def language(self, language: Optional[str]):
		self.__language = language


class Weather(OWM):
	def __init__(self, city: Optional[str]):
		self.city = city

	async def get(self):
		async with aiohttp.ClientSession() as session:
			async with session.get(
					const.request_link.format(
							city=self.city,
							language=self.language,
							token=self.token
					)
			) as response:
				return await response.json(encoding='UTF-8')
