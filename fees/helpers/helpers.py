# General use helpers
import pandas as pd
from fees.classes.tree import *
from fees.const.const import *
import os


def get_csv_path(file):
    """
    Gets the path to the CSV file
    :return: String representing the path to the CSV file
    """
    return os.path.join(os.path.dirname(__file__), "..", "csv", file)


def load_csv(path):
    """
    Load CSV file into a Pandas DataFrame and proccesses it into a useable data structure
    :param path: Path to CSV file
    :return: Pandas DataFrame
    """
    data = pd.read_csv(path)
    return data


def request_department(root):
    """
    Asks user to select a department from the tree
    :param root: TreeNode representing the root of the tree
    :return: String representing the department
    """
    all_departments = root.children_data()
    dept = ''
    while True:
        print("Please select one of the Departments below:")
        for i, dept in enumerate(all_departments):
            print(str(i + 1) + ". " + dept)
        print(str(len(all_departments) + 1) + ". All")
        print(str(len(all_departments) + 2) + ". Exit")
        dept = input("Enter Department: ")
        if dept == str(len(all_departments) + 2) or dept.lower() == "exit":
            dept = ''
            break
        if dept == str(len(all_departments) + 1) or dept.lower() == "all":
            dept = 'all'
            break
        if dept.isdigit():
            try:
                dept = all_departments[int(dept) - 1]
            except IndexError:
                print("Please enter a valid Department")
                continue
        if dept not in all_departments:
            print("Please enter a valid Department")
            continue
        break

    return dept


def request_category(department):
    """
    Asks user to select a category from the tree
    :param department: TreeNode representing the department
    :return: String representing the category
    """
    cat = ''
    while True:
        print("Next, plese select among the categories:")
        all_categories = department.children_data()
        for i, cat in enumerate(all_categories):
            print(str(i + 1) + ". " + cat)
        print(str(len(all_categories) + 1) + ". All")
        print(str(len(all_categories) + 2) + ". Exit")
        cat = input("Enter Category: ")
        if cat == str(len(all_categories) + 2) or cat.lower() == "exit":
            cat = ''
            break
        if cat == str(len(all_categories) + 1) or cat.lower() == "all":
            cat = 'all'
            break
        if cat.isdigit():
            try:
                cat = all_categories[int(cat) - 1]
            except IndexError:
                print("Please enter a valid Category")
                continue
        if cat not in all_categories:
            print("Please enter a valid Category")
            continue
        break

    return cat


def request_sub_category(category):
    """
    Asks user to select a sub category from the tree
    :param category: TreeNode representing the category
    :return: String representing the sub category
    """
    sub_cat = ''
    while True:
        print("Next, select among one of these Sub Categories:")
        all_sub_categories = category.children_data()
        for i, sub_cat in enumerate(all_sub_categories):
            print(str(i + 1) + ". " + sub_cat)
        print(str(len(all_sub_categories) + 1) + ". All")
        print(str(len(all_sub_categories) + 2) + ". Exit")
        sub_cat = input("Enter Sub Category: ")
        if sub_cat == str(len(all_sub_categories) + 2) or sub_cat.lower() == "exit":
            sub_cat = ''
            break
        if sub_cat == str(len(all_sub_categories) + 1) or sub_cat.lower() == "all":
            sub_cat = 'all'
            break
        if sub_cat.isdigit():
            try:
                sub_cat = all_sub_categories[int(sub_cat) - 1]
            except IndexError:
                print("Please enter a valid Sub Category")
                continue
        if sub_cat not in all_sub_categories:
            print("Please enter a valid Sub Category")
            continue
        break

    return sub_cat


def request_type(sub_category):
    """
    Asks user to select a type from the tree
    :param sub_category: TreeNode representing the sub category
    :return: String representing the type
    """
    type = ''
    while True:
        print("Finally, select among one of these Types:")
        all_types = sub_category.children_data()
        for i, type in enumerate(all_types):
            print(str(i + 1) + ". " + type)
        print(str(len(all_types) + 1) + ". All")
        print(str(len(all_types) + 2) + ". Exit")
        type = input("Enter Type: ")
        if type == str(len(all_types) + 2) or type.lower() == "exit":
            type = ''
            break
        if type == str(len(all_types) + 1) or type.lower() == "all":
            type = 'all'
            break
        if type.isdigit():
            try:
                type = all_types[int(type) - 1]
            except IndexError:
                print("Please enter a valid Type")
                continue
        if type not in all_types:
            print("Please enter a valid Type")
            continue
        break

    return type


def generate_confirmation(dept, cat, sub_cat, type):
    """
    Generates a confirmation message for the user. Mostly a helper function to reduce code on main.py
    :param dept: String representing the department
    :param cat: String representing the category
    :param sub_cat: String representing the sub category
    :param type: String representing the type
    :return: None
    """

    print("You wish to query fees for the following:")
    print("Department(s): " + str(dept))
    print("Category(s): " + str(cat))
    print("Sub-Category(s): " + str(sub_cat))
    print("Type(s): " + str(type))
    print("Is this correct? (Y/N)")
