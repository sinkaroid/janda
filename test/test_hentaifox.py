import unittest
from janda import Hentaifox, resolve

class TestMock(unittest.IsolatedAsyncioTestCase):

    async def test_hentaifox_get(self):
        hentaifox = Hentaifox()
        data = await hentaifox.get(59026)
        resolved = resolve(data)
        print(resolved)

        self.assertIsInstance(resolved, dict)
        self.assertTrue(resolved.get("success"))

if __name__ == "__main__":
    unittest.main()
