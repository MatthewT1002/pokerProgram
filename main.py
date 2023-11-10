import random


def shuffle():
    global deck
    global num
    for suit in ['\u2663', '\u2660', '\u2665', '\u2666']:
        for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            deck.append(suit + rank)
    card = random.choice(deck)
    deck.remove(card)
    playerCards.append(card)
    print(deck)


def dealerShuffle():
    global deck
    for dealerC in range(5):
        card = random.choice(deck)
        deck.remove(card)
        dealerCards.append(card)


deck = []
playerCards = []
dealerCards = []
num = 0

num = int(input("Enter number of players:"))

for playersHands in range(num * 2):
    shuffle()

if num > 0:
    print()
else:
    print("Enter valid number of players!!")
