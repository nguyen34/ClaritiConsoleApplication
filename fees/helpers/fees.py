# Helper file for fee processing

from fees.const.const import *
from fees.helpers.helpers import *


def sum_fees(tree):
    '''
        Sums up the fees in a tree given a Node as the root
        :param tree: TreeNode representing the root of the fees tree
        :return: float representing the total fees at a certain node in the tree
    '''
    if not tree.children:
        return tree.data
    else:
        return sum([sum_fees(child) for child in tree.children])


def calculate_fees(price, quantity, surcharge):
    '''
        Calculates the fees given a price, quantity, and surcharge
        :param price: float representing the price of the item
        :param quantity: int representing the quantity of the item
        :param surcharge: float representing the surcharge of the item
        :return: float representing the total fees of the item
    '''
    return price * quantity * (1 + surcharge)


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

        # Calculate the fee here. Pre-calculate the surcharge here and store it in their tree.
        # Under the impression that surcharges are automatically applied based on the department
        # so the amount should not change regardless of the query made
        # TODO: Improvement: Create a separate parameter to apply surcharge?
        surcharge = DEPT_SURCHARGES[dept] if DEPT_SURCHARGES[dept] else 0
        total_fee = calculate_fees(
            row["Unit_Price__c"], row["Quantity__c"], surcharge)
        fee_node = TreeNode(total_fee)

        if dept not in root.children_data():
            dept_node = TreeNode(dept)
            root.add_child(dept_node)
        else:
            dept_node = root.find_child(dept)
        if cat not in dept_node.children_data():
            cat_node = TreeNode(cat)
            dept_node.add_child(cat_node)
        else:
            cat_node = dept_node.find_child(cat)
        if sub_cat not in cat_node.children_data():
            sub_cat_node = TreeNode(sub_cat)
            cat_node.add_child(sub_cat_node)
        else:
            sub_cat_node = cat_node.find_child(sub_cat)
        if type not in sub_cat_node.children_data():
            type_node = TreeNode(type)
            sub_cat_node.add_child(type_node)
        else:
            type_node = sub_cat_node.find_child(type)
        type_node.add_child(fee_node)
    return root
