# Print out menu options for the user
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# Main function to manage the shopping list interactively
def main():
    shopping_list = [] # Initialize an empty list
    while True:
        display_menu()
        choice = input("Enter option: ")
        if choice == '1':
            add_item(shopping_list)
            # Prompt for and add an item
            pass
        elif choice == '2':
            remove_item(shopping_list)
            # Prompt for and remove an item
            pass
        elif choice == '3':
            view_list(shopping_list)
            # Display the shopping list
            pass
        elif choice == '4':
              print("Goodbye!")
              break
        else:
              print("Invalid choice. Please try again.")

# Function to add items to the list
def add_item(shopping_list):
    item = input("Enter the name of item you want to add: ") # Prompt user
    shopping_list.append(item)
    print(f"{item} added to the shopping list.")

# Function to remove items from the list
def remove_item(shopping_list):
    item = input("Enter the name of the item yo want to remove: ") #Prompt user
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the list.")
    else:
        print(f"{item} is not in the list.")    

# Function to display the current list
def view_list(shopping_list):
    if shopping_list:
        print(f"shopping_list: ")
        for index, item in enumerate (shopping_list, start = 1):
            print(f"{index}. {item}")
    else:
        print("Shopping_list is empty")

# Execute the script
if __name__ == "__main__":
    main()                