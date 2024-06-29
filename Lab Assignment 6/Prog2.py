# Create a program that acts as a simple contact manager. Allow users 
# to add contacts with their names and phone numbers. Use a dictionary 
# with names as keys and phone numbers as values. Implement 
# functionalities to add, delete, and search for contacts.
def display_menu():
    print("\nContact Manager")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. Display All Contacts")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def add_contact(contacts):
    name = input("Enter contact name: ")
    if name in contacts:
        print("Contact already exists.")
    else:
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print(f"Contact {name} added successfully.")

def delete_contact(contacts):
    name = input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print("Contact not found.")

def search_contact(contacts):
    name = input("Enter contact name to search: ")
    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]}")
    else:
        print("Contact not found.")

def display_contacts(contacts):
    if contacts:
        print("\nAll Contacts:")
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("No contacts available.")

def main():
    contacts = {}
    while True:
        choice = display_menu()
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            delete_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            display_contacts(contacts)
        elif choice == '5':
            print("Exiting the Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
