from fees.fees import *
from fees.helpers.helpers import *
from fees.const import *
import os


def get_csv_path():
    return os.path.join(os.path.dirname(__file__), "fees", "csv", "raw_fees.csv")


def main():
    csv_path = get_csv_path()
    data = load_csv(csv_path)
    tree = process_fees_csv_into_a_tree(data)
    tree.print_tree()


main()
