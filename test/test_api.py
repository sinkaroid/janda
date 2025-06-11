import aiohttp
import unittest

from janda.utils.client import list_api

class TestAPI(unittest.IsolatedAsyncioTestCase):

    async def test_api_endpoints(self):
        async with aiohttp.ClientSession() as session:
            for api in list_api():
                if "nhen" in api:
                    get_random = api + "/get?book=577774"
                elif "hentai2read" in api:
                    get_random = api + "/search?key=futanari"
                elif "simply-hentai" in api:
                    get_random = api + "/get?book=fate-grand-order/fgo-sanbunkatsuhou/all-pages"
                else:
                    get_random = api + "/random"

                async with session.get(get_random) as resp:
                    print(get_random, resp.status)
                    self.assertEqual(resp.status, 200, msg=f"{get_random} returned {resp.status}")

if __name__ == "__main__":
    unittest.main()
