import unittest
from fees.helpers.fees import *


class TestFees(unittest.TestCase):

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

    def test_sum_fees(self):
        self.type.add_child(TreeNode(1))
        self.type.add_child(TreeNode(2))
        self.assertEqual(sum_fees(self.root), 3)
        self.assertEqual(sum_fees(self.department), 3)
        self.assertEqual(sum_fees(self.category), 3)
        self.assertEqual(sum_fees(self.sub_category), 3)
        self.assertEqual(sum_fees(self.type), 3)

    def test_calculate_fees(self):
        self.assertEqual(calculate_fees(1, 1, 0), 1)
        self.assertEqual(calculate_fees(1, 1, 0.1), 1.1)
        self.assertEqual(calculate_fees(1, 2, 0.1), 2.2)
        self.assertEqual(calculate_fees(2, 2, 0.1), 4.4)
        self.assertEqual(calculate_fees(2, 2, 0), 4)
        self.assertEqual(calculate_fees(2, 2, -0.1), 3.6)
        self.assertEqual(calculate_fees(2, 2, -0.2), 3.2)

    def test_process_fees_csv_into_a_tree(self):
        data = load_csv(get_csv_path("raw_fees.csv"))
        self.assertIsNotNone(process_fees_csv_into_a_tree(data))


if __name__ == '__main__':
    unittest.main()
