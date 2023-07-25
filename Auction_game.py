# Initialize an empty dictionary to store bidder names and their corresponding bid amounts.
Bid_info = {}

# Set the bidding_finished flag to False, to indicate that the bidding process hasn't finished yet.
bidding_finished = False


# Function to find the highest bidder and display the winner with their bid amount.
def find_high_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


# Loop to collect bidder names and bid prices until bidding_finished becomes True.
while not bidding_finished:
    # Ask the user for their name and store it in 'bidder_name'.
    bidder_name = input("What is your name please? : ")

    # Ask the user for the bid price and convert it to a float, then store it in 'bid_price'.
    bid_price = float(input("Please! Enter the bid price:"))

    # Add the bidder's name and bid price to the Bid_info dictionary.
    Bid_info[bidder_name] = bid_price

    # Ask the user if there are any other bidders, and store the response in 'should_continue'.
    should_continue = input("Are there any other bidders? Type 'yes' or 'no':")

    if should_continue == 'no':
        # If there are no other bidders, set bidding_finished to True to exit the loop.
        bidding_finished = True

        # Loop through the Bid_info dictionary and print each bidder's name and bid price.
        for key in Bid_info:
            print(key)
            print(bid_price)
    elif should_continue == 'yes':
        # If there are other bidders, clear the Bid_info dictionary and continue the loop.
        Bid_info.clear()







