def show_menu():
    while True:
        print("******** PASSWORD MANAGER ********")
        print("1. Add New Password")
        print("2. View All Passwords")
        print("3. Search Password")
        print("4. Delete Password")
        print("5. Exit")

        choice = input("\nEnter your choice(1-5) : ").strip()

        if not choice:
            print("\nInvalid choice, no empty strings allowed.\n")
            continue

        if not choice.isdigit():
            print("\nInvalid choice, only digits are allowed.\n")
            continue

        if choice not in ["1", "2", "3", "4", "5"]:
            print("\nInvalid choice, please enter a number between 1 to 5.\n")
            continue

        if choice == "1":
            add_new_password()
        elif choice == "2":
            view_all_passwords()
        elif choice == "3":
            search_password()
        elif choice == "4":
            delete_password()
        elif choice == "5":
            print("Thank you.")
            break


def add_new_password():
    website = str(input("\nEnter the website : ")).strip()
    if not website:
        print("\nInvalid website, no empty strings are allowed.\n")
        return

    username = str(input("Enter the username : ")).strip()
    if not username:
        print("\nInvalid username, no empty strings are allowed.\n")
        return

    password = str(input("\nEnter the password : ")).strip()
    if not password:
        print("\nInvalid password, no empty strings are allowed.\n")
        return

    with open("passwords.txt", "a") as f:
        f.write(f"{website}|{username}|{password}\n")

    print("Password added successfully.\n")


def view_all_passwords():
    try:
        with open("passwords.txt", "r") as f:
            data = f.read().splitlines()

    except FileNotFoundError:
        print("\nNo passwords found.\n")
        return

    if not data:
        print("\nThis file is empty.\n")
        return

    print("\n******** PASSWORDS ********")
    for line in data:
        website, username, password = line.split("|")

        print(f"Website   : {website}")
        print(f"Username  : {username}")
        print(f"Password  : {password}")
        print("-" * 25)


def search_password():
    website_search = input("\nEnter the website : ").strip()

    if not website_search:
        print("\nInvalid input, no empty strings are allowed.\n")
        return

    try:
        with open("passwords.txt", "r") as f:
            data = f.read().splitlines()

    except FileNotFoundError:
        print("\nNo passwords found.\n")
        return

    if not data:
        print("\nThis file is empty.\n")
        return

    found = False
    print("\n****** Matching Results ******")
    for line in data:
        website, username, password = line.split("|")

        if (
            website_search.lower() == website.lower()
            or website_search.lower() in website.lower()
        ):
            found = True

            print(f"Website   : {website}")
            print(f"Username  : {username}")
            print(f"Password  : {password}")
            print("-" * 25)

    if not found:
        print("\nNo matching results found.\n")


def delete_password():
    website_delete = input("\nEnter the website to delete : ").strip()
    if not website_delete:
        print("\nInvalid input, no empty strings are allowed.\n")
        return

    try:
        with open("passwords.txt", "r") as f:
            data = f.read().splitlines()

    except FileNotFoundError:
        print("\nNo passwords found.\n")
        return

    if not data:
        print("\nThis file is empty.\n")
        return

    data_after_deletion = []

    match_found = 0

    for line in data:
        website, username, password = line.split("|")

        if (
            website_delete.lower() == website.lower()
            or website_delete.lower() in website.lower()
        ):
            match_found += 1
        else:
            data_after_deletion.append(line)

    if match_found == 0:
        print("\nNo match found.\n")
        return
    else:
        print(f"{match_found} matching entries found.\n")
        print("****** Matching Entries ******")

        for line in data:
            website, username, password = line.split("|")

            if (
                website_delete.lower() == website.lower()
                or website_delete.lower() in website.lower()
            ):
                print(f"Website   : {website}")
                print(f"Username  : {username}")
                print(f"Password  : {password}")
                print("-" * 25)

        delete_confirmation = input(
            "\nAre you sure you want to delete these entries? (yes/no) :"
        ).strip()

        if delete_confirmation.lower() == "yes":
            with open("passwords.txt", "w") as f:
                for line in data_after_deletion:
                    f.write(f"{line}\n")
            print(f"{match_found} password deleted sucessfully.\n")
        else:
            print("Password deletion aborted.")


show_menu()
