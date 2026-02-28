def ask_for_age():
    # function takes user input and returns integer
    age = int(input("What is your age? "))  # prompts user for input and converts it to an int
    return age

def can_they_vote(age):
    # check if user is eligible to vote
    if age >= 18:
        print("You can vote.")
    else:
        print("You are not eligible to vote.")

can_they_vote(ask_for_age())  # use the result of calling the function ask_for_age() as an argument