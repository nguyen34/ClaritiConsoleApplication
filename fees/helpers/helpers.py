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
