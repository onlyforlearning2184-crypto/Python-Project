def main_menu():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Category-wise Summary")
        print("4. Total Expense")
        print("5. Exit")

        choice = input("Enter your choice : ").strip()
        if not choice.isnumeric() or choice not in "12345":
            print("Invalid choice. Please select between 1 and 5 numbers.")
            continue

        if choice == "1":
            add_expense()
        if choice == "2":
            view_expense()
        if choice == "3":
            category_wise_summary()
        if choice == "4":
            total_expense()
        if choice == "5":
            print("Thank you.")
            break


def add_expense():
    with open("expenses.txt", "a") as f:
        category = input("Enter the expense category : ").strip().lower()
        amount = input(f"Enter the amount of {category} : ")
        if not amount.isnumeric():
            print("Invalid amount! please enter a number.")
            return
        else:
            f.write(f"{category},{amount}")
            f.write("\n")
            print("Expense added successfully.\n")


def view_expense():
    try:
        with open("expenses.txt", "r") as f:
            data = f.read().splitlines()

    except FileNotFoundError:
        print("File not found!")

    if len(data) == 0:
        print("File is empty, Add expense first")
        return
    else:
        print("All Expenses: ")
        print("-" * 20)
        for exp in data:
            parts = exp.split(",")
            category_part = parts[0]
            amount_part = int(parts[1])
            print(f"{category_part:<10}:{amount_part}")


def category_wise_summary():
    try:
        with open("expenses.txt", "r") as f:
            data = f.read().splitlines()
    except FileNotFoundError:
        print("File not found!")

    if len(data) == 0:
        print("File is empty, Add expense first.")
        return
    else:
        exps = {}
        print("Category-wise Summary: ")
        print("-" * 20)
        for exp in data:
            parts = exp.split(",")
            category_part = parts[0]
            amount_part = int(parts[1])
            if category_part not in exps:
                exps[category_part] = amount_part
            else:
                exps[category_part] += amount_part

        for key in exps:
            print(f"{key:<10} :{exps[key]}")


def total_expense():
    try:
        with open("expenses.txt", "r") as f:
            data = f.read().splitlines()

    except FileNotFoundError:
        print("File not found!")
    if len(data) == 0:
        print("File is empty, Add expense first.")
        return
    else:
        total = 0
        for exp in data:
            parts = exp.split(",")
            amount_part = int(parts[1])
            total += amount_part
        print(f"Total Expense: {total} ")


main_menu()
