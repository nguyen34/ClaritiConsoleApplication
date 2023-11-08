# Additional Tentative Classes for now. Will Deprecate later if not needed.

class Department:
    def __init__(self, name, surcharge):
        self.name = name
        self.surcharge = surcharge

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Category:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class SubCategory:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Type:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Fee:
    def __init__(self, quantity, unit_price, surcharge):
        self.quantity = quantity
        self.unit_price = unit_price
        self.total = quantity * unit_price * (1 + surcharge)
