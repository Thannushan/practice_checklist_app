from checklist_src.user import User
from checklist_src.item import Item


def main():
    user = User("John", "Smith")
    grocery_list = user.create_new_checklist("grocery list")
    grocery_list.add_item_to_list(Item("Apple"))
    grocery_list.print_my_checklist()

    stationary_list = user.create_new_checklist("stationary list")
    stationary_list.add_item_to_list(Item("Mechanical Pencil", 2))
    stationary_list.print_my_checklist()

    user.print_my_checklists()
    print(user)


if __name__ == "__main__":
    main()
