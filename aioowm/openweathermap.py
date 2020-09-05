from typing import Optional


class OWM:

	def __init__(self, token: Optional[str]):
		"""
		:param token: your api-key https://home.openweathermap.org/api_keys
		"""
		self.token = token
