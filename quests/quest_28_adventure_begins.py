def forest():
    print("You enter a dark forest.")
    choice = input("Do you go left or right? ")

    if choice.lower() == "left":
        print("You find a hidden treasure! You win!")
    else:
        print("You fall into a trap. Game over.")


def castle():
    print("You approach an old castle.")
    choice = input("Do you enter or run away? ")

    if choice.lower() == "enter":
        print("You meet a wise wizard who grants you powers! You win!")
    else:
        print("You safely return home. The adventure ends.")


print("Welcome to the Adventure!")
start = input("Do you choose the forest or the castle? ")

if start.lower() == "forest":
    forest()
else:
    castle()
