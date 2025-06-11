import unittest
from janda import Nhentai

class TestNhentai(unittest.IsolatedAsyncioTestCase):

    async def test_nhentai_get(self):
        nhentai = Nhentai()
        data = await nhentai.get(255369)
        print(data)  # Optional for debugging output

        self.assertIsInstance(data, dict)
        self.assertIn("id", data)
        self.assertEqual(data.get("id"), 255369)

if __name__ == "__main__":
    unittest.main()
