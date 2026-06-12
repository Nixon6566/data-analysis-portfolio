'''
Create a simple math flashcard game that asks a user what two
numbers added together equal and tell them whether or not they
got the answer correct.
'''


import random

def math_flashcard_game():
    print("Welcome to the Math Flashcard Game!")
    score = 0
    rounds = 5  # Number of questions

    for i in range(rounds):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        correct_answer = num1 + num2

        print(f"\nQuestion {i+1}: What is {num1} + {num2}?")
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Incorrect. The correct answer was {correct_answer}.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

    print(f"\nGame Over! You got {score} out of {rounds} correct.")

# Run the game
math_flashcard_game()