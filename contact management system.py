import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}
    return contacts

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=2)

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    contacts[name] = {"Phone": phone, "Email": email}
    save_contacts(contacts)
    print(f"\nContact {name} added successfully!\n")

def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.\n")
    else:
        print("\nContacts:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}")
        print()

def edit_contact(contacts):
    name = input("Enter the name of the contact you want to edit: ")

    if name in contacts:
        print(f"\nEditing contact: {name}")
        phone = input(f"Enter new phone number for {name}: ")
        email = input(f"Enter new email address for {name}: ")

        contacts[name]["Phone"] = phone
        contacts[name]["Email"] = email
        save_contacts(contacts)
        print(f"\nContact {name} updated successfully!\n")
    else:
        print(f"\nContact {name} not found.\n")

def delete_contact(contacts):
    name = input("Enter the name of the contact you want to delete: ")

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"\nContact {name} deleted successfully!\n")
    else:
        print(f"\nContact {name} not found.\n")

def contact_management_system():
    contacts = load_contacts()

    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

        input("Press Enter to continue...")

if __name__ == "__main__":
    contact_management_system()
