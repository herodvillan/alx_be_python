def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item = input("Enter the item to add: ")
            shopping_list.append(add_item)
            # Prompt for and add an item
        elif choice == '2':
            if not shopping_list:
                print("There is no item on the list.")
            else:
                remove_item = input("Enter the item to remove: ")
                if remove_item in shopping_list:
                    shopping_list.remove(remove_item)
        elif choice == '3':
            print(shopping_list)

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
