import unittest
from janda import Hentai2read, resolve

class TestHentai2read(unittest.IsolatedAsyncioTestCase):

    async def test_hentai2read_get(self):
        hentairr = Hentai2read()
        data = await hentairr.get("jeanne_alter_wants_to_mana_transfer/1")
        resolved = resolve(data)
        print(resolved)

        self.assertIsInstance(resolved, dict)
        self.assertIn("data", resolved)
        self.assertIn("title", resolved["data"])

if __name__ == "__main__":
    unittest.main()
