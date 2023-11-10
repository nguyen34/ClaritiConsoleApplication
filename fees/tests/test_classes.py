import unittest
from fees.classes.tree import *
from fees.classes.classes import *


class TestClasses(unittest.TestCase):
    def test_department_class(self):
        dept = Department("Marketing", 0.10)
        self.assertEqual(dept.name, "Marketing")
        self.assertEqual(dept.surcharge, 0.10)
        self.assertEqual(str(dept), "Marketing")

    def test_fee_class(self):
        fee = Fee(1, 1, 0)
        self.assertEqual(fee.quantity, 1)
        self.assertEqual(fee.unit_price, 1)
        self.assertEqual(fee.total, 1)
        surcharge_fee = Fee(1, 1, 0.10)
        self.assertEqual(surcharge_fee.quantity, 1)
        self.assertEqual(surcharge_fee.unit_price, 1)
        self.assertEqual(surcharge_fee.total, 1.1)


class TestTreeClasses(unittest.TestCase):
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

    def test_tree_node(self):
        self.assertEqual(self.root.data, "Fees")
        self.assertEqual(self.root.children[0].data, "Marketing")
        self.assertEqual(self.department.children[0].data, "ABM")
        self.assertEqual(self.category.children[0].data, "Tier 1")
        self.assertEqual(self.sub_category.children[0].data, "Cat1")
        self.assertEqual(self.type.data, "Cat1")

    def test_add_and_remove_child(self):
        self.root.add_child(TreeNode("Support"))
        self.assertEqual(len(self.root.children), 2)
        self.root.remove_child(self.root.children[0])
        self.assertEqual(len(self.root.children), 1)
        self.assertEqual(self.root.children[0].data, "Support")

    def test_get_level(self):
        self.assertEqual(self.root.get_level(), 0)
        self.assertEqual(self.department.get_level(), 1)
        self.assertEqual(self.category.get_level(), 2)
        self.assertEqual(self.sub_category.get_level(), 3)
        self.assertEqual(self.type.get_level(), 4)

    def test_children_data(self):
        self.assertEqual(self.root.children_data(), ["Marketing"])
        self.assertEqual(self.department.children_data(), ["ABM"])
        self.assertEqual(self.category.children_data(), ["Tier 1"])
        self.assertEqual(self.sub_category.children_data(), ["Cat1"])
        self.assertEqual(self.type.children_data(), [])
        self.root.add_child(TreeNode("Support"))
        self.assertEqual(self.root.children_data(), ["Marketing", "Support"])

    def test_find_child(self):
        self.assertEqual(self.root.find_child("Marketing"), self.department)
        self.assertEqual(self.department.find_child("ABM"), self.category)
        self.assertEqual(self.category.find_child("Tier 1"), self.sub_category)
        self.assertEqual(self.sub_category.find_child("Cat1"), self.type)

        self.assertIsNone(self.type.find_child("Cat2"))
        self.assertIsNotNone(self.type.find_child("Cat1"))

        self.assertIsNone(self.root.find_child("Support"))
        new_department_node = TreeNode("Support")
        self.root.add_child(new_department_node)
        self.assertEqual(self.root.find_child("Support"), new_department_node)
        self.assertEqual(self.root.find_child("support"), new_department_node)
        self.assertEqual(self.root.find_child("SUPport"), new_department_node)
