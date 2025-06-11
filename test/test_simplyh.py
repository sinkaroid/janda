import unittest
from janda import SimplyHentai, resolve

class TestMock(unittest.IsolatedAsyncioTestCase):

    async def test_simplyh_get(self):
        simplyh = SimplyHentai()
        data = await simplyh.get("fate-grand-order/perros/all-pages")
        resolved = resolve(data)
        print(resolved)

        self.assertIsInstance(resolved, dict)
        self.assertTrue(resolved.get("success"))

if __name__ == "__main__":
    unittest.main()
