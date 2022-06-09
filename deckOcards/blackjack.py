from deck import deck

#player 1, computer 2
playerHand = 0
computerHand = 0

def main():
    global playerHand
    global computerHand
    deck1 = deck()
    deck1.shuffle()
    deal(deck1)
    displayHand(playerHand, 1)

    print('--------------------')
    print('Hit? (Y/N): ')
    x = input()
   
    if x.upper() == 'Y':
        while x.upper() == 'Y':
            print('--------------------')
            print('player delt: ')
            playerHand += deck1.hit(True)
            if blackjack(playerHand):
                print('BLACKJACK! PLAYER WINS')
                quit()
            elif busted(playerHand):
                print('PLAYER BUSTED! DEALER WINS')
                quit()
            print('--------------------')
            displayHand(playerHand, 1)
            print('Hit? (Y/N): ')
            x = input()
    
    print('--------------------')
    print('Dealer flips:',computerHand)
    print('--------------------')
    if blackjack(computerHand):
        print('BLACKJACK! DEALER WINS')
    elif computerHand > playerHand:
        print('DEALER WINS')
    elif computerHand < 17:
        while computerHand < 17:
            if blackjack(computerHand):
                print('BLACKJACK! DEALER WINS')
            print('--------------------')
            print('dealer delt: ')
            computerHand += deck1.hit(True)
            print('--------------------')
            print('dealer new total:',computerHand)
            if blackjack(computerHand):
                print('BLACKJACK! DEALER WINS')
            elif busted(computerHand):
                print('DEALER BUSTED! PLAYER WINS')
    if computerHand == playerHand:
        print('DRAW')    



def deal(deck):
    global playerHand
    global computerHand
    
    print('player delt: ')
    playerHand += deck.hit(True)
    print('--------------------')
    print('computer delt: ')
    computerHand += deck.hit(True)
    print('--------------------')
    print('player delt: ')
    playerHand += deck.hit(True)
    print('--------------------')
    print('computer delt: ???')
    computerHand += deck.hit(False)
    print('--------------------')

def displayHand(hand, who):
    if who == 1:
        print('Player total:',hand)
    else:
        print('Computer Total:',hand)

def busted(hand):
    if hand > 21:
        return True
    return False

def blackjack(hand):
    if hand == 21:
        return True
    return False


if __name__ == "__main__":
    main()