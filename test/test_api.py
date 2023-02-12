import aiohttp
import asyncio
from janda.utils.client import list_api

async def test_api():
    async with aiohttp.ClientSession() as session:
        for api in list_api():
            if "nhen" in api:
                get_random = api + "/get?book=177013"
            elif "hentai2read" in api:
                get_random = api + "/search?key=futanari"
            elif "simply-hentai" in api:
                get_random = api + "/get?book=fate-grand-order/fgo-sanbunkatsuhou/all-pages"
            else:
                get_random = api + "/random"
            async with session.get(get_random) as resp:
                print(get_random, resp.status)

asyncio.run(test_api())