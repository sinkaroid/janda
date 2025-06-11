import unittest
from janda import Asmhentai, resolve

class TestMock(unittest.IsolatedAsyncioTestCase):

    async def test_asmhen_get(self):
        asmhen = Asmhentai()
        data = await asmhen.get(311851)
        resolved = resolve(data)
        print(resolved)

        self.assertIsInstance(resolved, dict)
        self.assertTrue(resolved.get("success"))

if __name__ == "__main__":
    unittest.main()
