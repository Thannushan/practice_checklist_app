class Checklist:
    """
    This class contains items that a user wants to keep track of in a list
    """

    def __init__(self, name):
        self.name = name
        self.my_list = []

    def add_item_to_list(self, item):
        self.my_list.append(item)

    def print_my_checklist(self):
        for item in self.my_list:
            print(item)

    def __str__(self):
        return "%s" % self.name

