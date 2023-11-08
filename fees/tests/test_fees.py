import unittest
from fees.fees import *


class TestFees(unittest.TestCase):

    def test_calculate_fees(self):
        self.assertEqual(calculate_fees(
            "Marketing", "ABM", "Tier 1", "New"), 0)


if __name__ == '__main__':
    unittest.main()
