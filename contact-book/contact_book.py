def show_menu():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice : ").strip()
        if not choice.isnumeric() or choice not in "123456":
            print("Invalid choice. Please select between 1 and 6 numbers.")
            continue

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break


def add_contact():
    name = input("Enter the contact name  : ").strip().title()
    phone_number = input(f"Enter the phone-number of {name} : ").strip()
    if not phone_number.isnumeric():
        print("Invalid PhoneNumber! please enter in numbers.")
        return

    try:
        with open("contacts.txt", "r") as f:
            contacts = f.read().splitlines()

    except FileNotFoundError:
        contacts = []

    for contact in contacts:
        parts = contact.split(",")
        existing_name = parts[0]
        if name.lower() == existing_name.lower():
            print("Contact already exists, no duplicate contact allowed.")
            return

    with open("contacts.txt", "a") as f:
        f.write(f"{name},{phone_number}\n")

    print("Contact added successfully.")


def view_contacts():
    try:
        with open("contacts.txt", "r") as f:
            contacts = f.read().splitlines()

    except FileNotFoundError:
        print("No contacts found.")
        return
    if len(contacts) == 0:
        print("No contacts found.")
        return
    else:
        print("All Contacts: ")
        print("-" * 20)
        for c in contacts:
            parts = c.split(",")
            contact = parts[0]
            phone_number = parts[1]
            print(f"{contact}:{phone_number}")

    print("Contact updated successfully.")


def search_contact():
    search_term = input("Enter search term: ").strip().lower()

    try:
        with open("contacts.txt", "r") as f:
            contacts = f.read().splitlines()
    except FileNotFoundError:
        print("No contacts found.")
        return

    matching_contact_found = False
    print("Matching Contacts")
    print("-" * 25)

    for c in contacts:
        contact, phone_number = c.split(",")

        if search_term in contact.lower():
            print(f"{contact:<10} : {phone_number}")
            matching_contact_found = True

    if not matching_contact_found:
        print("No matching contact found.")


def update_contact():
    u_name = input("Enter contact name to update : ").strip().title()

    try:
        with open("contacts.txt", "r") as f:
            contacts = f.read().splitlines()

    except FileNotFoundError:
        print("No contacts found.")
        return
    if len(contacts) == 0:
        print("No contacts found.")
        return

    updated_contacts = []
    found = False
    new_phone_number = input("Enter new phone-number : ").strip()

    if not new_phone_number.isnumeric():
        print("Invalid PhoneNumber! please enter in numbers.")
        return

    for c in contacts:
        existing_contact, phone_number = c.split(",")

        if existing_contact.lower() == u_name.lower():
            updated_contacts.append(f"{existing_contact},{new_phone_number}")
            found = True
        else:
            updated_contacts.append(c)

    if not found:
        print("Contact not found.")
        return

    with open("contacts.txt", "w") as f:
        for line in updated_contacts:
            f.write(line + "\n")

    print("contact updated successfully.")


def delete_contact():
    name = input("Enter contact name to delete : ").strip().title()
    try:
        with open("contacts.txt", "r") as f:
            contacts = f.read().splitlines()

    except FileNotFoundError:
        print("No contacts found.")
        return
    if len(contacts) == 0:
        print("No contacts found.")
        return

    contacts_dele = []
    found = False

    for contact in contacts:
        contact_name, phone = contact.split(",")
        if name.lower() == contact_name.lower():
            found = True
        else:
            contacts_dele.append(f"{contact_name},{phone}")

    if not found:
        print("Contact not found.")
        return

    with open("contacts.txt", "w") as f:
        for line in contacts_dele:
            f.write(line + "\n")

    print("contact deleted successfully.")
