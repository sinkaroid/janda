import unittest
from janda import Thentai, resolve

class TestMock(unittest.IsolatedAsyncioTestCase):

    async def test_thentai_get(self):
        thentai = Thentai()
        data = await thentai.get(608979)
        resolved = resolve(data)
        print(resolved)

        self.assertIsInstance(resolved, dict)
        self.assertTrue(resolved.get("success"))

if __name__ == "__main__":
    unittest.main()
