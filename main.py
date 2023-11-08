from fees.fees import *
from fees.helpers.helpers import *
from fees.const import *
import os


def get_csv_path():
    return os.path.join(os.path.dirname(__file__), "fees", "csv", "raw_fees.csv")


def main():
    # Pre-process the CSV file into a tree to be ready for the console application
    csv_path = get_csv_path()
    data = load_csv(csv_path)
    tree = process_fees_csv_into_a_tree(data)
    # Main console body
    while True:
        print("Welcome to the Fees Calculator! Here, we shall calculate the total fees for a given query.")

        dept = request_department()
        if not dept:
            break
        if dept.lower() == 'all':
            dept = DEPARTMENTS[:-1]

        # TODO: Use the tree to get the caregories/children of the department
        cat = request_category()
        if not cat:
            break
        if cat.lower() == 'all':
            cat = CATEGORIES[:-1]

        sub_cat = request_sub_category()
        if not sub_cat:
            break
        if sub_cat.lower() == 'all':
            sub_cat = SUB_CATEGORIES[:-1]

        type = request_type()
        if not type:
            break
        if type.lower() == 'all':
            type = TYPES[:-1]

        # TODO: Re-factor into a helper function
        print("You wish to query fees for the following:")
        print("Department(s): " + str(dept))
        print("Category(s): " + str(cat))
        print("Sub-Category(s): " + str(sub_cat))
        print("Type(s): " + str(type))
        print("Is this correct? (Y/N)")
        confirmation = input()
        if confirmation.lower() == 'y' or confirmation.lower() == 'yes':
            total_fees = query_fees(tree)
            print("Total Fees: " + str(total_fees))
        else:
            print("Please try again.")
            continue
        print("Would you like to make another query? (Y/N)")
        confirmation = input()
        if confirmation.lower() == 'y' or confirmation.lower() == 'yes':
            continue
        else:
            break
    print("Thank you for using the Fees Calculator. Goodbye!")
    return


main()
