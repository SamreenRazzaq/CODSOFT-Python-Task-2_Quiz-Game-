#QUIZ GAME:

import random

#Load Quz Questions
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["New York", "London", "Paris", "Dublin"],
        "answer": "3" 
    },
    {
        "question": "Who is CEO of Tesla?",
        "choices": ["Jeff Berzos", "Elon Musk", "Bill Gates", "Tony Stark"],
        "answer": "2" 
    },
    {
        "question": "The iPhone was created by which company?",
        "choices": ["Apple", "Intel", "Amazon", "Microsoft"],
        "answer": "1" 
    },
    {
        "question": "How many Harry Potter books are there?",
        "choices": ["1", "4", "6", "7"],
        "answer": "4" 
    },
]

#Present Quiz Question
def present_question(question):
    print(question["question"])
    for index, choice in enumerate(question["choices"], start=1):
        print(f"{index}. {choice}")
    user_answer = input("Enter answer (1,2,3,4): ")
    return user_answer

#Evaluate the User's Answer
def evaluate_answer(question, user_answer):
    correct_answer = question["answer"]
    if user_answer.lower() == correct_answer.lower():
        return True
    return False

#Display Welcome Message and Rules
def quiz_game():
    print("Welcome to the Quiz Game!")
    print("Let's get started!\n")

    score = 0
    for question in quiz_questions:
        user_answer = present_question(question)
        is_correct = evaluate_answer(question, user_answer)

        if is_correct:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {question['answer']}\n")

    print("Quiz Completed!")
    print(f"Your final score is: {score} out of {len(quiz_questions)}")

    if score == len(quiz_questions):
        print("Congratulations! You got all the questions right.")
    elif score >= len(quiz_questions) / 2:
        print("Good job! You did well.")

#Play Again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        quiz_game()
    else:
        print("Thank you for playing the Quiz Game!")

if __name__ == "__main__":
    quiz_game()
