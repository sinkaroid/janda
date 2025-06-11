import unittest
from janda import Nhentai, resolve

class TestMock(unittest.IsolatedAsyncioTestCase):

    async def test_nhentai_get(self):
        nhentai = Nhentai()
        data = await nhentai.get(255369)
        resolved = resolve(data)
        print(resolved)

        self.assertIsInstance(resolved, dict)
        self.assertTrue(resolved.get("success"))

if __name__ == "__main__":
    unittest.main()
