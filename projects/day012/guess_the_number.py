from art import logo

import random

print(logo)

answer = random.choice(range(1, 101))

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
win = False
lose = False

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

while not win or lose:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempts -= 1
    if attempts == 0:
        lose = True
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        win = True

if win:
    print(f"You got it! The answer was {answer}.")
else:
    print("You've run out of guesses. You lose.")
