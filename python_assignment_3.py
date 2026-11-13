"""
Python Assignment 3: While Loop, For Loop and Functions
"""

import random


# ---------------------------------------------------------------
# 1. While loop & control statements: Number Guessing Game
# ---------------------------------------------------------------
def number_guessing_game():
    secret_number = random.randint(1, 10)   # random number between 1 and 10
    attempts = 3                            # maximum number of valid guesses

    while attempts > 0:
        guess = int(input("Guess the number (between 1 and 10): "))

        # Out-of-range guess: inform the user and skip the rest of the loop
        if guess < 1 or guess > 10:
            print("Your guess is out of range. Please guess a number between 1 and 10.")
            continue

        # Only valid guesses use up an attempt
        attempts -= 1

        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            break
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print("Too low. Try again.")
    else:
        # Runs only if the loop ended without 'break' (no attempts left)
        print("Better luck next time!")
        print("The correct number was:", secret_number)


# ---------------------------------------------------------------
# 2. For loop: Multiplication Table Generator
# ---------------------------------------------------------------
def multiplication_table():
    number = int(input("Enter the number for which you want the multiplication table: "))

    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")


# ---------------------------------------------------------------
# 3. Function: BMI Calculator
# ---------------------------------------------------------------
def calculate_bmi(weight, height):
    """Return BMI = weight (kg) / height (m) squared."""
    return weight / (height ** 2)


def bmi_calculator():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi:.2f}")


# ---------------------------------------------------------------
# Run all three programs
# ---------------------------------------------------------------
if __name__ == "__main__":
    print("=== Number Guessing Game ===")
    number_guessing_game()

    print("\n=== Multiplication Table Generator ===")
    multiplication_table()

    print("\n=== BMI Calculator ===")
    bmi_calculator()
