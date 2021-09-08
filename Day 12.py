from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def checkAnswer(guess, answer, turns):
    if guess > answer:
        print("Guess is too high.")
        return turns -1
    elif guess < answer:
        print("Guess is too low.")
        return turns -1
    else:
        print(f"You got it! The answer is {answer}")

def setDifficulty():
    level = input("Choose a difficulty, 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    answer = randint(1,100)

    turns = setDifficulty()
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess; "))

        turns = checkAnswer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()
