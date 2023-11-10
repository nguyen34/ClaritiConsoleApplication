# Additional Tentative Classes for now. Will Deprecate later if not needed.

class Department:
    # This class would be important to keep if we wanted to apply a surcharge more dynamically on each query
    # TODO: Improvement: Use this class in the tree generation to have access to surcharge if needed.
    def __init__(self, name, surcharge):
        self.name = name
        self.surcharge = surcharge

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Fee:
    # TODO: Improvement: Use this class in the tree generation to make this implementation more sophisticated and allow for more complex queries.
    def __init__(self, quantity, unit_price, surcharge):
        self.quantity = quantity
        self.unit_price = unit_price
        self.total = quantity * unit_price * (1 + surcharge)
