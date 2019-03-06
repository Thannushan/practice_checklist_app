from checklist_src.checklist import Checklist


class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.checklist = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def create_new_checklist(self, name):
        my_new_checklist = Checklist(name)
        self.checklist.append(my_new_checklist)
        return my_new_checklist

    def print_my_checklists(self):
        for i in range(0, len(self.checklist)):
            print("%d. %s" % (i+1, self.checklist[i]))
