import unittest
from response.request import Request

class TestRequest(unittest.TestCase):
    def test_constructor_valid(self):
        obj = Request()

if __name__ == "__main__":
    unittest.main()