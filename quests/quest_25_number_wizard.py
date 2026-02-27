#!/usr/bin/python3

import random

def number_wizard():
    secret_number = random.randint(1, 100)
    guessed_correctly = False

    print("Welcome to the Number Wizard! ")
    print("I have chosen a number between 1 and 100. Can you guess it?")

    while not guessed_correctly:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number! ")
            continue

        if guess == secret_number:
            print(f"Amazing! The number was {secret_number}. You guessed it!")
            guessed_correctly = True
        elif guess < secret_number:
            print("Too low! Try again. ")
        else:
            print("Too high! Try again. ")

number_wizard()
