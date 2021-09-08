from os import system, name

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')

def findHighestBidder(biddingRecord):
    highestBid = 0
    winner = ""
    for bidder in biddingRecord:
        bidAmount = biddingRecord[bidder]
        if bidAmount > highestBid:
            highestBid = bidAmount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highestBid}")

print(logo)

bids = {}
biddingFinished = False

while not biddingFinished:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    shouldContinue = input("Are there any other bidders? Type 'yes' or 'no':\n")
    if shouldContinue == "no":
        biddingFinished = True
        findHighestBidder(bids)
    elif shouldContinue == "yes":
        clear()

