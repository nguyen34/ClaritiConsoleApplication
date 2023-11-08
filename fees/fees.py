from fees.const import *
from fees.helpers.helpers import *


def calculate_fees(dept, cat, sub_cat, type):
    return 0

# TODO: Use generator comprehension  to save on memory?


def query_fees(tree):
    '''
        Queries the fees tree given user input
        :param tree: TreeNode representing the root of the fees tree
        :return: float representing the total fees from the given query
    '''
    print("Welcome to the Fees Calculator!")
    tree.print_tree()
    return 0
