import random
from card import card

class deck:
    deck = []
    suits = ["clubs", "spades", "hearts", "diamonds"]
    #jack = 11, queen = 12, ect...
    values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
    for suit in suits:
        for value in values:
            deck.append(card(suit, value))


    def shuffle(self):
        random.shuffle(self.deck)

    def hit(self):
        print(deck[0].value)
        self.deck.pop(0)
        print(deck[0].value)