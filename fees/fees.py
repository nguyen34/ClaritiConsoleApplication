from fees.const import *


def calculate_fees(dept, cat, sub_cat, type):
    return 0


def query_fees():
    dept = ""
    cat = ""
    sub_cat = ""
    type = ""
    while True:
        print("Welcome to the Fees Calculator!")
        print('''To get started, please select one of the Departments below:
                1. Marketing
                2. Sales
                3. Development
                4. Operations
                5. Support
                6. Exit
            ''')
        dept = input("Enter Department: ")
        if dept == "6" or dept.lower() == "exit":
            print("Thank you for using the Fees Calculator!")
            break

        if dept.isdigit():
            dept = DEPARTMENTS[int(dept) - 1]

        if dept not in DEPARTMENTS:
            print("Please enter a valid Department")
          # TODO: Re-prompt user for input
            continue

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
                11. Exit
            ''')

        cat = input("Enter Category: ")

        if cat == "11" or cat.lower() == "exit":
            print("Thank you for using the Fees Calculator!")
            break

        if cat.isdigit():
            cat = CATEGORIES[int(cat) - 1]

        if cat not in CATEGORIES:
            print("Please enter a valid Category")
            # TODO: Re-prompt user for input
            continue

        print(
            '''Next, select among one of these Sub Categories:
              1. Cat 1
              2. Cat 2
              3. Cat 3
              4. Exit
            ''')

        sub_cat = input("Enter Sub Category: ")

        if sub_cat == "4" or sub_cat.lower() == "exit":
            print("Thank you for using the Fees Calculator!")
            break

        if sub_cat.isdigit():
            sub_cat = SUB_CATEGORIES[int(sub_cat) - 1]

        if sub_cat not in SUB_CATEGORIES:
            print("Please enter a valid Sub Category")
            # TODO: Re-prompt user for input
            continue

        print('''Finally, please select among these types: 
                1. Type A
                2. Type B
                3. Type C
                4. Exit
              ''')

        type = input("Enter Type: ")

        if type == "4" or type.lower() == "exit":
            print("Thank you for using the Fees Calculator!")
            break

        if type.isdigit():
            type = TYPES[int(type) - 1]

        if type not in TYPES:
            print("Please enter a valid Type")

        print("Calculating fees for Department: {}, Caregory: {}, Sub Category: {} and Type: {}".format(
            dept, cat, sub_cat, type))
