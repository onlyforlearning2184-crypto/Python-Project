def show_menu():
    while True:
        print("\nStudent Record Manager")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Student Report (Total, Average, Grade)")
        print("4. Top Scorer")
        print("5. Update Student Marks")
        print("6. Delete Student")
        print("7. Exit")

        choice = input("Enter your choice(1-7): ").strip()
        if not choice.isdigit():
            print("Invalid input! Please enter a number between 1 and 7.")
            continue
        if choice not in "1234567":
            print("Invalid choice! Please select between 1 and 7.")
            continue

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            student_report()
        elif choice == "4":
            top_scorer()
        elif choice == "5":
            update_student_marks()
        elif choice == "6":
            delete_student()
        elif choice == "7":
            print("Goodbye!")
            break


def add_student():

    roll_number = input("Enter the roll number: ").strip()
    name = input("Enter the name: ").strip().title()
    marks = input("Enter marks: ").strip()

    if not roll_number.isdigit():
        print("Invalid roll number! Please enter a number.")
        return

    if not marks.isdigit():
        print("Invalid marks! Please enter a number.")
        return

    if int(marks) < 0 or int(marks) > 100:
        print("Invalid marks! Enter value between 0 and 100.")
        return

    if not name:
        print("Invalid name! Name can never be empty.")
        return

    try:
        with open("students.txt", "r") as f:
            data = f.read().splitlines()

    except FileNotFoundError:
        data = []

    for lines in data:
        parts = lines.split(",")
        roll_num = parts[0]

        if roll_num == roll_number:
            print("Student with this roll number already exists.")
            return

    with open("students.txt", "a") as w:
        w.write(f"{roll_number},{name},{marks}\n")

    print("Student added successfully.")


def view_students():
    try:
        with open("students.txt", "r") as f:
            data = f.read().splitlines()

        if len(data) == 0:
            print("No student records available.")
            return
    except FileNotFoundError:
        print("No student records found.")
        return

    for lines in data:
        roll_no, name, marks = lines.split(",")
        print(f"Roll No: {roll_no} | Name: {name} | Marks: {marks}")


def student_report():
    roll_number = input("Enter the roll number: ").strip()

    if not roll_number.isdigit():
        print("Invalid roll number! Please enter a number.")
        return

    try:
        with open("students.txt", "r") as f:
            data = f.read().splitlines()

        if len(data) == 0:
            print("No student records available.")
            return
    except FileNotFoundError:
        print("No student records found.")
        return

    found = False
    for lines in data:
        roll_num, name, marks = lines.split(",")
        marks = int(marks)
        if roll_num == roll_number:
            print(f"Roll No: {roll_num}")
            print(f"Name: {name}")
            print(f"Marks: {marks}")
            average = float(marks)
            print(f"Average: {average}")
            if marks >= 90:
                print("Grade: A")
            elif marks >= 75:
                print("Grade: B")
            elif marks >= 60:
                print("Grade: C")
            elif marks < 60:
                print("Grade: D")
            found = True
            break

    if not found:
        print("Student not found.")


def top_scorer():

    try:
        with open("students.txt", "r") as f:
            data = f.read().splitlines()

        if len(data) == 0:
            print("No student records available.")
            return
    except FileNotFoundError:
        print("No student records found.")
        return

    maximum_marks = 0
    for lines in data:
        marks = int(lines.split(",")[2])
        if marks > maximum_marks:
            maximum_marks = marks

    for values in data:
        roll_num, name, mark = values.split(",")
        mark = int(mark)
        if mark == maximum_marks:
            print("Top Scorer")
            print(f"Roll No: {roll_num}")
            print(f"Name: {name}")
            print(f"Marks: {mark}")
            if mark >= 90:
                print("Grade: A")
            elif mark >= 75:
                print("Grade: B")
            elif mark >= 60:
                print("Grade: C")
            elif mark < 60:
                print("Grade: D")
            break

    # maximum_marks = -1
    # for lines in data:
    #     roll_num, name, marks = lines.split(",")
    #     marks = int(marks)
    #     if marks > maximum_marks:
    #         maximum_marks = marks
    #         top_roll = roll_num
    #         top_name = name
    # print("Top Scorer")
    # print(f"Roll No: {top_roll}")
    # print(f"Name: {top_name}")
    # print(f"Marks: {maximum_marks}")
    # if maximum_marks >= 90:
    #     print("Grade: A")
    # elif maximum_marks >= 75:
    #     print("Grade: B")
    # elif maximum_marks >= 60:
    #     print("Grade: C")
    # elif maximum_marks < 60:
    #     print("Grade: D")


def update_student_marks():
    roll_number = input("Enter the roll number: ").strip()

    if not roll_number.isdigit():
        print("Invalid roll number! Please enter a number.")
        return

    try:
        with open("students.txt", "r") as f:
            data = f.read().splitlines()

        if len(data) == 0:
            print("No student records available.")
            return
    except FileNotFoundError:
        print("No student records found.")
        return

    new_marks = input("Enter new marks: ").strip()

    if not new_marks.isdigit():
        print("Invalid marks! Please enter a number.")
        return

    if int(new_marks) < 0 or int(new_marks) > 100:
        print("Invalid marks! Enter value between 0 and 100.")
        return

    updated_data = []
    found = False
    for lines in data:
        roll_no, name, marks = lines.split(",")
        if roll_no == roll_number:
            updated_data.append(f"{roll_no},{name},{new_marks}")
            found = True
        else:
            updated_data.append(lines)

    if not found:
        print("Student not found.")
        return

    with open("students.txt", "w") as f:
        for line in updated_data:
            f.write(f"{line}\n")

    print("Student marks updated successfully.")


def delete_student():
    roll_number = input("Enter roll number: ").strip()

    if not roll_number.isdigit():
        print("Invalid roll number! Please enter a number.")
        return

    try:
        with open("students.txt", "r") as f:
            data = f.read().splitlines()

        if len(data) == 0:
            print("No student records available.")
            return
    except FileNotFoundError:
        print("No student records found.")
        return

    data_updation = []
    found = False
    for lines in data:
        roll_no = lines.split(",")[0]
        if roll_no == roll_number:
            found = True
        else:
            data_updation.append(lines)

    if not found:
        print("Student not found.")
        return

    with open("students.txt", "w") as f:
        for line in data_updation:
            f.write(f"{line}\n")

    print("Student deleted successfully.")
