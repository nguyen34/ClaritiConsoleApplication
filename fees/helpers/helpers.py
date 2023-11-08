import pandas as pd
from fees.classes.tree import *
from fees.const import *

# Dummy function for unit tests


def add(x, y):
    return x + y


def load_csv(path):
    """
    Load CSV file into a Pandas DataFrame and proccesses it into a useable data structure
    :param path: Path to CSV file
    :return: Pandas DataFrame
    """
    data = pd.read_csv(path)
    return data


def process_fees_csv_into_a_tree(data):
    """
    Processes a Pandas DataFrame into a tree structure
    :param data: Pandas DataFrame
    :return: TreeNode
    """
    root = TreeNode("Fees")
    for _, row in data.iterrows():
        dept = row["Department__c"]
        cat = row["Category__c"]
        sub_cat = row["Sub_Category__c"]
        type = row["Type__c"]

        # Calculate the fee here
        surcharge = DEPT_SURCHARGES[dept] if DEPT_SURCHARGES[dept] else 0
        total_fee = row["Quantity__c"] * row["Unit_Price__c"] * (1 + surcharge)
        fee_node = TreeNode(total_fee)

        if dept not in root.children:
            dept_node = TreeNode(dept)
            root.add_child(dept_node)
        else:
            dept_node = root.children[root.children.index(dept)]
        if cat not in dept_node.children:
            cat_node = TreeNode(cat)
            dept_node.add_child(cat_node)
        else:
            cat_node = dept_node.children[dept_node.children.index(cat)]
        if sub_cat not in cat_node.children:
            sub_cat_node = TreeNode(sub_cat)
            cat_node.add_child(sub_cat_node)
        else:
            sub_cat_node = cat_node.children[cat_node.children.index(sub_cat)]
        if type not in sub_cat_node.children:
            type_node = TreeNode(type)
            sub_cat_node.add_child(type_node)
        else:
            type_node = sub_cat_node.children[sub_cat_node.children.index(
                type)]
        type_node.add_child(fee_node)
    return root


def request_department():
    dept = ''
    while True:
        print('''Please select one of the Departments below:
                    1. Marketing
                    2. Sales
                    3. Development
                    4. Operations
                    5. Support
                    6. All
                    7. Exit
                ''')
        dept = input("Enter Department: ")
        if dept == "7" or dept.lower() == "exit":
            dept = ''
            break
        if dept.isdigit():
            dept = DEPARTMENTS[int(dept) - 1]
        if dept not in DEPARTMENTS:
            print("Please enter a valid Department")
            continue
        break

    return dept


def request_category():
    cat = ''
    while True:
        print('''Next, plese select a Category:
                    1. ABM
                    2. Pre Sales
                    3. Sales Engineering
                    4. Coding
                    5. Quality Assurance
                    6. Human Resources
                    7. Performance Management
                    8. Tier 1
                    9. Tier 2
                    10. Tier 3
                    11. All
                    12. Exit
                ''')
        cat = input("Enter Category: ")
        if cat == "12" or cat.lower() == "exit":
            cat = ''
            break
        if cat.isdigit():
            cat = CATEGORIES[int(cat) - 1]
        if cat not in CATEGORIES:
            print("Please enter a valid Category")
            continue
        break

    return cat


def request_sub_category():
    sub_cat = ''
    while True:
        print('''Next, select among one of these Sub Categories:
                    1. Cat 1
                    2. Cat 2
                    3. Cat 3
                    4. All
                    5. Exit
                ''')
        sub_cat = input("Enter Sub Category: ")
        if sub_cat == "5" or sub_cat.lower() == "exit":
            sub_cat = ''
            break
        if sub_cat.isdigit():
            sub_cat = SUB_CATEGORIES[int(sub_cat) - 1]
        if sub_cat not in SUB_CATEGORIES:
            print("Please enter a valid Sub Category")
            continue
        break

    return sub_cat


def request_type():
    type = ''
    while True:
        print('''Next, select among one of these Types:
                    1. Type 1
                    2. Type 2
                    3. Type 3
                    4. All
                    5. Exit
                ''')
        type = input("Enter Type: ")
        if type == "5" or type.lower() == "exit":
            type = ''
            break
        if type.isdigit():
            type = TYPES[int(type) - 1]
        if type not in TYPES:
            print("Please enter a valid Type")
            continue
        break

    return type
