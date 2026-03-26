import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



def highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid amount of Rs.{highest_bid}.")

logo = '''
                         ___________
                         \'         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\'
                         `'-------'`
                       .-------------.
                      /_______________\' '''


auction = {}

print(logo)
print("\n"*2)
bidding = True
while bidding:
    name = input("Enter name: ")
    amount = int(input("Enter the bidding amount: "))
    auction[name] = amount
    clear_screen()
    continue_bidding = input("Are there any other bidders?(Yes/No): ").lower()
    if continue_bidding == "no":
        bidding = False
        highest_bidder(auction)