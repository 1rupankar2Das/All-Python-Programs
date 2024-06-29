# Develop a quiz game where questions are stored in a dictionary. Each 
# question should have its corresponding answer. Allow the user to select 
# a category, then randomly select a question from that category. 
# Prompt the user for an answer and check if it's correct.
import random

def display_menu(categories):
    print("\nQuiz Game")
    print("Select a category:")
    for i, category in enumerate(categories.keys(), 1):
        print(f"{i}. {category}")
    print(f"{len(categories) + 1}. Exit")
    choice = input("Enter your choice: ")
    return choice

def ask_question(category, questions):
    question = random.choice(list(questions[category].keys()))
    answer = questions[category][question]
    user_answer = input(f"\n{question}\nYour answer: ")
    if user_answer.strip().lower() == answer.lower():
        print("Correct!")
    else:
        print(f"Wrong. The correct answer is: {answer}")

def main():
    questions = {
        "Science": {
            "What is the chemical symbol for water?": "H2O",
            "How many planets are in our solar system?": "8",
        },
        "Geography": {
            "What is the capital of France?": "Paris",
            "Which country is known as the Land of the Rising Sun?": "Japan",
        },
        "History": {
            "Who was the first president of the United States?": "George Washington",
            "In which year did the Titanic sink?": "1912",
        }
    }
    
    while True:
        choice = display_menu(questions)
        if choice.isdigit() and 1 <= int(choice) <= len(questions):
            category = list(questions.keys())[int(choice) - 1]
            ask_question(category, questions)
        elif choice == str(len(questions) + 1):
            print("Exiting the Quiz Game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
