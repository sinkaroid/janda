import unittest
from janda import Pururin, resolve

class TestMock(unittest.IsolatedAsyncioTestCase):

    async def test_pururin_get(self):
        pururin = Pururin()
        data = await pururin.get(47226)
        resolved = resolve(data)
        print(resolved)

        self.assertIsInstance(resolved, dict)
        self.assertTrue(resolved.get("success"))

if __name__ == "__main__":
    unittest.main()
