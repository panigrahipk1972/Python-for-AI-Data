#   map() (for transforming values) and reduce() (for combining values).  
# Using map to square numbers
from functools import reduce
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)
# Using reduce to calculate the product of numbers
product = reduce(lambda x, y: x * y, numbers)
print(product)
#Create a Calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid input. Please try again.")

calculator()
import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    while True:
        number = random.randint(1, 100)
        attempts = 0

        while True:
            try:
                guess = int(input("Guess a number between 1 and 100: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            attempts += 1

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                break

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye 👋")
            break

number_guessing_game()

#Rock-Paper-Scissors game
def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    while True:
        user = input("Enter your choice (rock, paper, scissors): ").lower()
        if user in choices:
            break
        else:
            print("Invalid input. Please enter rock, paper, or scissors.")

    print(f"Computer chose: {computer}")
    print(f"You chose: {user}")

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

rock_paper_scissors()
