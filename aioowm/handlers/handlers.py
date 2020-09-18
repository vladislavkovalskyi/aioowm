async def language(language: str):
	"""
	:param language: accepts language identifier (ru, en, fr)
	:return: True if lang in identifiers. False if lang not in identifiers
	"""

	identifiers = ("af", "al", "ar", "az", "bg", "ca", "cz", "da", "de", "el", "en", "eu",
	               "fa", "fi", "fr", "gl", "he", "hi", "hr", "hu", "id", "it", "ja", "kr",
	               "la", "lt", "mk", "no", "nl", "pl", "pt", "pt_br", "ro", "ru", "sv", "se",
	               "sk", "sl", "sp", "es", "sr", "th", "tr", "ua", "uk", "vi", "zh_cn", "zn_tw",
	               "zu")

	if language.lower() not in identifiers:
		raise TypeError("Unknown language identifier!")
	else:
		return language.lower()


async def temperature(temperature: str):
	"""
	:param temperature: accepts temp identifier (celsius, fahrenheit, kelvin)
	:return: units
	"""
	identifiers = {"celsius": "metric", "fahrenheit": "imperial", "kelvin": "kelvin"}

	if temperature not in identifiers:
		raise TypeError("Unknown temperature identifier!")
	else:
		return identifiers[temperature]
