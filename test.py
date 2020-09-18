from asyncio import run

from aioowm import OWM

weather = OWM(token="Your token here",
              language="ru")


async def app():
	result = await weather.get("Moscow")
	print(result)

run(app())
