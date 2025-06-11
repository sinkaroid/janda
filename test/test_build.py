import unittest
import janda

class TestVersion(unittest.TestCase):

    def test_version(self):
        print(janda.__version__)
        self.assertIsInstance(janda.__version__, str)
        self.assertRegex(janda.__version__, r"^\d+\.\d+\.\d+$")

if __name__ == "__main__":
    unittest.main()
