# guessing game
secret_number = 37
user_input = 0

while user_input != secret_number:
    user_input = input("Guess a number between 1 and 100: ")

if user_input == secret_number:
    print("You guessed correctly!")