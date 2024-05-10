import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
game = [True]

while game[0] == True:

    userCards = []
    userValue = 0

    dealerCards = []
    dealerValue = 0
    stand = [False]

    def AssignCards(Cards, Value):
        for i in range(2):
            randomNumber = random.randint(0,12)
            Cards.append(cards[randomNumber])
        for card in Cards:
            if card == "J" or card == "Q" or card == "K":
                Value += 10
            elif card == "A":
                Value += 11
            else:
                Value += card
        return Value

    userValue = AssignCards(userCards, userValue)
    dealerValue = AssignCards(dealerCards, dealerValue)
    dealerCards[1] = "?"

    def printStats():
        print(f"TOTAL VALUE: {userValue}")
        print(f"TOTAL CARDS: {userCards}")
        print()
        #print(dealerValue)
        print(f"DEALER CARDS {dealerCards}")
        print()

    printStats()

    while userValue < 21 and not stand[0]:
        UserInput = input("Choose either hit (h) or stand (s)")
        print(f"You have entered {UserInput.lower()}")

        def UserAction(userCards, input, Value):
            global stand
            if input == "h":
                randomNumber = random.randint(0,12)
                userCards.append(cards[randomNumber])
                Value = 0
                for card in userCards:
                    if card == "J" or card == "Q" or card == "K":
                        Value += 10
                    elif card == "A":
                        Value += 11
                    else:
                        Value += card
            elif input == "s":
                stand[0] = True
            else:
                print("input valid option")

            return Value
        
        def dealerAction(dealerCards, Value):
            randomNumber = random.randint(0,12)
            dealerCards.append(cards[randomNumber])
            if dealerCards[-1] == "J" or dealerCards[-1] == "Q" or dealerCards[-1] == "K":
                Value += 10
            elif dealerCards[-1] == "A":
                Value += 11
            else:
                Value += dealerCards[-1]
            dealerCards[-1] = "?"
            
            return Value



        userValue = UserAction(userCards, UserInput.lower(), userValue)
        if dealerValue < 17:
            dealerValue = dealerAction(dealerCards, dealerValue)
        printStats() 
        #print(dealerValue)

    if dealerValue == 21 and userValue == 21:
        print("Draw, player bets are returned")
    elif userValue > 21:
        print("Player Loses")
    elif dealerValue > 21 and userValue <= 21:
        print("Player Wins")
    elif dealerValue < userValue:
        print("Player Wins")
    elif dealerValue >= userValue:
        print("Player Loses")

    print(f"DEALER VALUE: {dealerValue}")

    if input("would you like to play again? (y) or (n)") == "n":
        game[0] = False








