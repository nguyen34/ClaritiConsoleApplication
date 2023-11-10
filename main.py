from fees.fees import *
from fees.helpers.helpers import *
from fees.const import *


def main():
    # Pre-process the CSV file into a tree to be ready for the console application
    csv_path = get_csv_path("raw_fees.csv")
    data = load_csv(csv_path)
    root = process_fees_csv_into_a_tree(data)
    # Main console body
    # Tracker variables to keep track of the current query
    dept = 'all'
    cat = 'all'
    sub_cat = 'all'
    type = 'all'
    while True:
        temp = root
        print("Welcome to the Fees Calculator! Here, we shall calculate the total fees for a given query.")

        dept = request_department(temp)
        if not dept:
            break

        if dept.lower() != 'all':
            temp = temp.find_child(dept)
            cat = request_category(temp)
            if not cat:
                break

        if cat.lower() != 'all':
            temp = temp.find_child(cat)
            sub_cat = request_sub_category(temp)
            if not sub_cat:
                break

        if sub_cat.lower() != 'all':
            temp = temp.find_child(sub_cat)
            type = request_type(temp)
            if not type:
                break

            if type.lower() != 'all':
                temp = temp.find_child(type)

        generate_confirmation(dept, cat, sub_cat, type)
        confirmation = input()
        if confirmation.lower() == 'y' or confirmation.lower() == 'yes':
            total_fees = sum_fees(temp)
            # Formats the total fees into a currency format for better readability
            print("Total Fees: " + str('${:,.2f}'.format(total_fees)))
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
