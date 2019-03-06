class Item:
    """
    This class contains the information about what the user wants to store as an item
    """

    def __init__(self, name, quantity=1):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return "%s:%d" % (self.name, self.quantity)
