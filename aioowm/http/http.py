from aiohttp import ClientSession

from typing import Optional


async def request(url: str, data: Optional[dict] = None) -> dict:
	async with ClientSession() as session:
		async with session.get(url=url, params=data) as response:
			return await response.json(encoding='UTF-8')
