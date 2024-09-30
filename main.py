# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
def find_winner(info):
    highest_bid = 0
    for bidder in bids:
        bid_value = info[bidder]
        if bid_value > highest_bid:
            highest_bid = bid_value
            winner = bidder
    print(f"The winner of the auction is: {winner} with {highest_bid} $ ")


print(logo)
print("Welcome to tonight's Blind auction!")

bids = {}

finished = False
while not finished:
    bidder = input("Please type your name: ")
    value = int(input("Place your bid: $ "))
    bids[bidder] = value
    should_continue = input("Are there any other bidders?\n").lower()
    if should_continue == "no":
        finished = True
        find_winner(bids)
    elif should_continue == "yes":
        print("\n" * 50)

