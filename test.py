from aioowm import OWM
from asyncio import run


async def app():
	weather = OWM('85163474e6db3515b4fc39c3439c7220', 'ru')
	result = await weather.get('Your City')
	print(result)

run(app())
