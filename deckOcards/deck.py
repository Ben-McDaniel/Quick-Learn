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

    def hit(self, show):
        if show:
            fancyDis = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
            print(str(fancyDis[self.deck[0].value - 2]) + ' of ' + self.deck[0].suit)
        correctVal = [2,3,4,5,6,7,8,9,10,10,10,10,11]
        retVal = correctVal[self.deck[0].value - 2]
        del self.deck[0]
        return retVal
