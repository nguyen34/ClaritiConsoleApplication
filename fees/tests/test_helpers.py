import unittest
import unittest.mock
from fees.helpers.helpers import *
from fees.classes.tree import TreeNode


class TestHelpers(unittest.TestCase):

    def setUp(self) -> None:
        self.root = TreeNode("Fees")
        self.root.add_child(TreeNode("Marketing"))
        self.department = self.root.children[0]
        self.department.add_child(TreeNode("ABM"))
        self.category = self.department.children[0]
        self.category.add_child(TreeNode("Tier 1"))
        self.sub_category = self.category.children[0]
        self.sub_category.add_child(TreeNode("Cat1"))
        self.type = self.sub_category.children[0]

    def test_get_csv_path(self):
        self.assertIsNotNone(get_csv_path("raw_fees.csv"))

    def test_load_csv(self):
        self.assertIsNotNone(load_csv(get_csv_path("raw_fees.csv")))
        self.assertIsNotNone(load_csv(get_csv_path("raw_fees.csv")))

    def test_request_department(self):
        with unittest.mock.patch('builtins.input', return_value="2"):
            self.assertEqual(request_department(self.root), "all")

        with unittest.mock.patch('builtins.input', return_value="marketing"):
            self.assertEqual(request_department(self.root), "marketing")

    def test_request_category(self):
        with unittest.mock.patch('builtins.input', return_value="2"):
            self.assertEqual(request_category(self.department), "all")

        with unittest.mock.patch('builtins.input', return_value="abm"):
            self.assertEqual(request_category(self.department), "abm")

    def test_request_sub_category(self):
        with unittest.mock.patch('builtins.input', return_value="2"):
            self.assertEqual(request_sub_category(self.category), "all")

        with unittest.mock.patch('builtins.input', return_value="tier 1"):
            self.assertEqual(request_sub_category(self.category), "tier 1")

    def test_request_type(self):
        with unittest.mock.patch('builtins.input', return_value="2"):
            self.assertEqual(request_type(self.sub_category), "all")

        with unittest.mock.patch('builtins.input', return_value="cat1"):
            self.assertEqual(request_type(self.sub_category), "cat1")


if __name__ == '__main__':
    unittest.main()
