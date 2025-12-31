def show_menu():
    while True:
        print("\n********QUIZ ENGINE********")
        print("1. Add Question")
        print("2. View All Questions")
        print("3. Start Quiz")
        print("4. View Scores")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if not choice.isdigit():
            print("Invalid input! please enter in digits.")
            continue
        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid input! please enter a number between 1 to 5.")
            continue

        if choice == "1":
            add_question()
        elif choice == "2":
            view_questions()
        elif choice == "3":
            start_quiz()
        elif choice == "4":
            view_scores()
        elif choice == "5":
            print("Thank you!")
            break


def add_question():
    question = input("Enter the question: ").strip()
    if question == "":
        print("Invalid question! no empty spaces allowed.")
        return

    option1 = input("Enter the option1: ").strip()
    if option1 == "":
        print("Invalid option1! no empty spaces allowed.")
        return

    option2 = input("Enter the option2: ").strip()
    if option2 == "":
        print("Invalid option2! no empty spaces allowed.")
        return

    option3 = input("Enter the option3: ").strip()
    if option3 == "":
        print("Invalid option3! no empty spaces allowed.")
        return

    option4 = input("Enter the option4: ").strip()
    if option4 == "":
        print("Invalid option4! no empty spaces allowed.")
        return

    if (
        option1 == option2
        or option1 == option3
        or option1 == option4
        or option2 == option3
        or option2 == option4
        or option3 == option4
    ):
        print("Invalid options! no duplicate options are allowed")
        return

    correct_option = input("Enter correct option number(1-4): ").strip()
    if not correct_option.isdigit():
        print("Invalid input! please enter in digits.")
        return

    if correct_option not in ["1", "2", "3", "4"]:
        print("Invalid choice! Correct option must be between 1 and 4.")
        return

    with open("questions.txt", "a") as f:
        f.write(
            f"{question} | {option1} | {option2} | {option3} | {option4} | {correct_option}\n"
        )

    print("Question added successfully!")


def view_questions():
    try:
        with open("questions.txt", "r") as f:
            data = f.read().splitlines()

    except FileNotFoundError:
        print("No questions available. Please add questions first.")
        return

    if not data:
        print("No questions available. Please add questions first.")
        return
    question_num = 1
    for lines in data:
        parts = lines.split("|")
        if len(parts) != 6:
            continue
        question = parts[0].strip()
        option1 = parts[1].strip()
        option2 = parts[2].strip()
        option3 = parts[3].strip()
        option4 = parts[4].strip()

        print(f"Q{question_num}. {question}")
        print(f" 1) {option1}")
        print(f" 2) {option2}")
        print(f" 3) {option3}")
        print(f" 4) {option4}")

        question_num += 1


def start_quiz():
    username = input("Enter the username: ").strip()
    if username == "":
        print("Invalid username! no empty spaces allowed.")
        return
    try:
        with open("questions.txt", "r") as f:
            data = f.read().splitlines()

    except FileNotFoundError:
        print("No questions available. Please add questions first.")
        return

    if not data:
        print("No questions available. Please add questions first.")
        return

    question_num = 0
    score = 0
    total_question = 0
    for lines in data:
        parts = lines.split("|")
        if len(parts) != 6:
            continue

        question_num += 1

        question = parts[0].strip()
        option1 = parts[1].strip()
        option2 = parts[2].strip()
        option3 = parts[3].strip()
        option4 = parts[4].strip()
        correct_option = parts[5].strip()

        print(f"Q{question_num}. {question}")
        print(f" 1) {option1}")
        print(f" 2) {option2}")
        print(f" 3) {option3}")
        print(f" 4) {option4}")
        total_question += 1

        while True:
            answer = input("Enter your answer(1-4): ").strip()
            if not answer.isdigit():
                print("Invalid input! please enter digits only.")
                continue

            if answer not in ["1", "2", "3", "4"]:
                print("Invalid choice! Correct option must be between 1 and 4.")
                continue
            break

        if correct_option == answer:
            score += 1

    if total_question == 0:
        print("All questions are malformed")
        return

    print("Quiz completed!")
    print(f"Your score: {score} / {total_question}")

    with open("scores.txt", "a") as a:
        a.write(f"{username} | {score} | {total_question}\n")


def view_scores():
    try:
        with open("scores.txt", "r") as f:
            data = f.read().splitlines()

    except FileNotFoundError:
        print("No scores available.")
        return

    if not data:
        print("No scores available.")
        return

    index = 0
    invalid_count = 0
    print("------- QUIZ SCORES -------")
    for lines in data:
        parts = lines.split("|")

        if len(parts) != 3:
            invalid_count += 1
            continue

        index += 1
        username = parts[0].strip()
        score = parts[1].strip()
        total = parts[2].strip()
        print(f"{index}. {username} : {score} / {total}")

    if invalid_count == 0:
        print("There's no invalid questions.")
    else:
        print(f"There's {invalid_count} invalid questions.")


show_menu()
