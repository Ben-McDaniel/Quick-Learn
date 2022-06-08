from deck import deck

playerHand = []
computerHand = []

def main():

    deck1 = deck()
    #for i in range (0,51):
    #    print(str(deck1.deck[i].value) + ' of ' + deck1.deck[i].suit)
    deck1.shuffle()
    #for j in range (0,51):
    #    print(str(deck1.deck[j].value) + ' of ' + deck1.deck[j].suit)
    
    #playerHand.append(deck1.hit)
    #displayHand(playerHand)
    temp = deck1.hit()




def deal(deck):
    for i in range (0,1):
        playerHand.append(deck.hit)
        computerHand.append(deck.hit)

def displayHand(hand):
    pass

if __name__ == "__main__":
    main()