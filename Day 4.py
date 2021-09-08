import random

game_choices = ["rock", "paper", "scissors"]
print("Welcome to Rock, Paper, Scissors!")

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n "))
print(f"You chose {game_choices[user_choice]}")

computer_choice = random.randint(0, 2)
print(f"Computer chose {game_choices[computer_choice]}")

if user_choice == computer_choice:
    print("Tie Game!")
elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 1) or (user_choice == 2 and computer_choice == 1):
    print("You Win!")
elif (user_choice < 0 or user_choice > 2):
    print("You Lose! Invalid choice!")
else:
    print("You Lose!")
