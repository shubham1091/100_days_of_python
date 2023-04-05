import os
import logo

def find_highest_bidder(bidding_record):
    winner =""
    highest_bid = 0
    for Bidder in bidding_record:
        if bidding_record[Bidder]> highest_bid:
            highest_bid= bidding_record[Bidder]
            winner = Bidder
    print(f"The winndr is {winner} with a bid of ${highest_bid}")


print(logo.gavel)

Bids = dict()
bidding_finished = False
print("Welcome to the secret quction program.")

while not bidding_finished:
    usr = input("What is your name?: ")
    bid = int(input("Whst's your bid?: $"))
    Bids[usr]=bid
    should_continue= input("Are there any other bidders? Type 'yes' or 'no.\n")
    os.system('cls')
    if should_continue == 'no':
        bidding_finished = True

find_highest_bidder(Bids)