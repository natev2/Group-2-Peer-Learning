direction = input("Go left or right? ")

if direction == "left":
    action = input("swim or wait? ")
    
    if action == "swim":
        print("You found the treasure!")
    else:
        print("You waited... nothing happened.")
        
elif direction == "right":
    print("You fell into a trap!")
    
else:
    print("Invalid choice.")
