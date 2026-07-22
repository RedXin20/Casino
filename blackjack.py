import random 

print("Select starting money")
balance = int(input())
print(f"Current Balance: {balance}")
print("Insert betting amount:")
bet = int(input())
if bet > balance:
    print("Insufficent balance")
else: 

    cards = [
    ("Ace of Hearts", 11), ("2 of Hearts", 2), ("3 of Hearts", 3), ("4 of Hearts", 4), ("5 of Hearts", 5),
    ("6 of Hearts", 6), ("7 of Hearts", 7), ("8 of Hearts", 8), ("9 of Hearts", 9), ("10 of Hearts", 10),

    ("Jack of Hearts", 10), ("Queen of Hearts", 10), ("King of Hearts", 10), ("Ace of Diamonds", 11), ("2 of Diamonds", 2),
    ("3 of Diamonds", 3), ("4 of Diamonds", 4), ("5 of Diamonds", 5), ("6 of Diamonds", 6), ("7 of Diamonds", 7),
    ("8 of Diamonds", 8), ("9 of Diamonds", 9), ("10 of Diamonds", 10), ("Jack of Diamonds", 10), ("Queen of Diamonds", 10),

    ("King of Diamonds", 10), ("Ace of Clubs", 11), ("2 of Clubs", 2), ("3 of Clubs", 3), ("4 of Clubs", 4),
    ("5 of Clubs", 5), ("6 of Clubs", 6), ("7 of Clubs", 7), ("8 of Clubs", 8), ("9 of Clubs", 9),
    ("10 of Clubs", 10), ("Jack of Clubs", 10), ("Queen of Clubs", 10), ("King of Clubs", 10), 
    
    ("Ace of Spades", 11), ("2 of Spades", 2), ("3 of Spades", 3), ("4 of Spades", 4), ("5 of Spades", 5), 
    ("6 of Spades", 6), ("7 of Spades", 7), ("8 of Spades", 8), ("9 of Spades", 9), ("10 of Spades", 10), 
    ("Jack of Spades", 10), ("Queen of Spades", 10), ("King of Spades", 10)
    ]

    dealerStatus = 0
    playerStatus = 0
    dealerNum = 0
    playerNum = 0
    gameStatus = 1

    def hit(totalNum, deck):
        randomCard = random.randrange(len(deck))
        draw = deck.pop(randomCard)
        print(draw[0])
        totalNum += draw[1]
        print(totalNum)

        return totalNum

    def dealerHit(dealerNum, deck):
        if dealerNum <= 16:
            dealerNum = hit(dealerNum, deck)

        return dealerNum

    # Game loop
    while gameStatus == 1: 
 
        # Picking card for player
        if playerNum == 0 and playerStatus == 0:
            playerNum = hit(playerNum, cards)
            playerNum = hit(playerNum, cards) 

        # Picking card for dealer
        if dealerStatus == 0:
            dealerNum = dealerHit(dealerNum, cards)
            if dealerNum > 16: 
                print(f"Dealer is standing at {dealerNum}")
                dealerStatus = 1 


        # Game conditions, checking busts
        if dealerNum > 21:
            print("Player wins! Dealer goes bust!")
            break
        
        if playerNum > 21:
            print("Dealer wins! Player goes bust!")
            break

        
        # Blackjack checks
        if dealerNum == 21 or playerNum == 21:
            if dealerNum == 21 and playerNum == 21:
                print("Draw!")
            elif dealerNum == 21:
                print("Dealer wins!")
            else:
                print("Player wins!")
            break
        
        # Checking stands
        if playerStatus == 1:
            if dealerStatus == 0:
                continue
            
            if playerNum > dealerNum:
                print("Player Wins!")
            elif playerNum < dealerNum:
                print("Dealer Wins!")
            else:
                print("Push!")
            break 

        print("Do you want to hit? (Y/N)")
        userInput = input()
        if userInput == "N":
            playerStatus = 1
            print(f"Player is standing at {playerNum}")
        else:
            print("Dealing more cards:")
            playerNum = hit(playerNum, cards)

