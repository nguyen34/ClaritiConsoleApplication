import unittest
from fees.helpers.helpers import add


class TestHelpers(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, 0), 0)


if __name__ == '__main__':
    unittest.main()
