import random

def calculateScore(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def dealCard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def compare(userScore, npcScore):
    if userScore == npcScore:
        return "Draw"
    elif npcScore == 0:
        return "You lose, NPC has Blackjack."
    elif userScore == 0:
        return "You win with Blackjack."
    elif userScore > 21:
        return "You went over. You lose."
    elif npcScore > 21:
        return "NPC went over. You win."
    elif userScore > npcScore:
        return "You win"
    else:
        return "You lose"

def playGame():
    userCards = []
    npcCards = []
    isGameOver = False

    for _ in range(2):
        userCards.append(dealCard())
        npcCards.append(dealCard())

    while not isGameOver:
        userScore = calculateScore(userCards)
        npcScore = calculateScore(npcCards)
        print(f" Your cards: {userCards}, current score: {userScore}")
        print(f" NPC's first card: {npcCards[0]}") 

        if userScore == 0 or npcScore == 0 or userScore > 21:
            isGameOver = True
        else:
            userChoice = input("Type 'y' to get another car or 'n' to hold: ")
            if userChoice == 'y':
                userCards.append(dealCard())
            else:
                isGameOver = True

    while npcScore != 0 and npcScore < 17:
        npcCards.append(dealCard())
        npcScore = calculateScore(npcCards)

    print(f"Your final hand: {userCards}, final score: {userScore}")
    print(f"NPC final hand: {npcCards}, final score: {npcScore}")
    print(compare(userScore, npcScore))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    playGame()
