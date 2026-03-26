logo = '''
 ____  _            _       _            _    
| __ )| | __ _  ___| | _   | | __ _  ___| | __
|  _ \| |/ _` |/ __| |/ /  | |/ _` |/ __| |/ /
| |_) | | (_| | (__|   < |_| | (_| | (__|   < 
|____/|_|\__,_|\___|_|\_\(_)___\__,_|\___|_|\_\\
'''
print(logo)

import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = input("Enter your name: ").title()

def deal_card():
    return random.choice(deck)

#Player's Hand
player_hand = []
player_hand.append(deal_card())
player_hand.append(deal_card())
print(f"{player}'s Hand:",player_hand)

#Dealer's Hand
dealer_hand = []
dealer_hand.append(deal_card())
dealer_hand.append(deal_card())
#Second card is hidden
print(f"Dealer's Hand: [{dealer_hand[0]}, '?']")

#calculating Ace as 11 or 1
def calculate_score(hand):
    total = sum(hand)
    if total > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        total = sum(hand)
    return total

#Calculating total in 1st round
player_total = calculate_score(player_hand)
print(f"{player}'s Total =",player_total)
dealer_total = calculate_score(dealer_hand)

#Player's Turn
game_over = False

while True:
    choice = input("Type 'Y' to hit(get another card), or type 'N' to stand(stop): ").lower()
    if choice == 'y':
        player_hand.append(deal_card())
        player_total = calculate_score(player_hand)
        if player_total > 21:
            print(f"{player}'s Hand:",player_hand)
            print(f"{player}'s Total =",player_total)
            print("Dealer's Hand:" ,dealer_hand)
            print("Dealer's Total = ",dealer_total)
            print("You are busted, Dealer Wins")
            game_over = True
            break
        elif player_total == 21:
            print(f"{player}'s Hand:",player_hand)
            print(f"{player}'s Total =",player_total)
            print("Dealer's Hand:" ,dealer_hand)
            print("Dealer's Total = ",dealer_total)
            print("You win!")
            game_over = True
            break
        else:
            print(f"{player}'s Hand:",player_hand)
            print(f"{player}'s Total =",player_total)
            print(f"Dealer's Hand: [{dealer_hand[0]}, '?']")


    elif choice == 'n':
        break
    else:
        print("Invalid Input")

#Dealer's Turn
if not game_over:
    while dealer_total < 17:
        dealer_hand.append(deal_card())
        dealer_total = calculate_score(dealer_hand)
        print("Dealer's Hand:",dealer_hand)
        print(f"Dealer's Total: {dealer_total}\n")

#Final Comparison
    print(f"{player}'s Hand:",player_hand)
    print("Dealer's Hand:" ,dealer_hand)
    print(f"{player}'s Total =",player_total)
    print("Dealer's Total = ",dealer_total)

    if dealer_total > 21:
        print("Dealer is busted! You win!")
    elif dealer_total > player_total:
        print("Dealer Wins!")
    elif dealer_total < player_total:
        print("You Win!")
    else:
        print("It's A Tie")