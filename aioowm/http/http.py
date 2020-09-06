from aiohttp import ClientSession


async def request(data):
	async with ClientSession() as session:
		async with session.get(data) as response:
			return await response.json(encoding='UTF-8')
