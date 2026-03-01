def ask_for_age():
    age = int(input("What is your age? "))
    return age

def can_they_vote(age):
    if age >= 18:
        print("You can vote.")
    else:
        print("You are not eligible to vote.")

can_they_vote(ask_for_age())