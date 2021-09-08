
print("Welcome to Treasure Island!")
print("Your mission is the find the treasure!")

choice1 = input("You are at a crossroad. Where would you like to go, left or right? ").lower()

if choice1 == "left":
    choice2 = input("You have come to a lake. There is an island in the middle of the lake. Would you like to wait or swim? ").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors: blue, green, and purple. Which color do you choose? ").lower()
        if choice3 == "green":
            print("You found a room with carnivorous plants. Game Over")
        elif choice3 == "blue":
            print("You found a room full of hostile pirates. Game Over")
        elif choice3 == "purple":
            print("You have found the treasure! You win!")
        else:
            print("Thar be dragons! Game Over")
    else:
        print("You got attacked by an aggressive minnow. Game Over.")
else:
    print("You fell into a hole. Game Over.")
