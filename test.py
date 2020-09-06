import asyncio

from aioowm import OWM

weather = OWM('85163474e6db3515b4fc39c3439c7220', 'ru')


async def run():
	result = await weather.get('Moscow')

	print(result)


asyncio.run(run())
