def display_question(question, correct_answer):
    answer = input(f"{question}\nYour answer: ")

    if answer.lower() == correct_answer.lower():
        print("Correct!\n")
    else:
        print(f"Incorrect. The correct answer was '{correct_answer}'.\n")


def main():
    """
    Main function to run the fill-in-the-blank quiz.
    """
    questions = [
        {"question": "The capital of India is ________.", "answer": "Paris"},
        {"question": "Water boils at ________ degrees Celsius.", "answer": "100"},
        {"question": "The largest planet in our solar system is ________.", "answer": "Jupiter"}
    ]

    print("Welcome to the Fill in the Blank Quiz!\n")
    for q in questions:
        display_question(q["question"], q["answer"])

if __name__ == "__main__":
    main()
