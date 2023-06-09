from os import system, name
import art


def clear():
    # clear Windows terminal/shell
    if name == 'nt':
        _ = system('cls')

    # mac and linux
    else:
        _ = system('clear')


def display_art():
    print(art.logo)


def get_user_bids(all_bids):  # all_bids should be a dictionary
    user_name = input("What is your name?: ")
    bid = input("What's your bid?: $")

    all_bids.update({user_name: bid})

    other_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    while other_bids == "yes":
        clear()
        user_name = input("What is your name?: ")
        bid = input("What's your bid?: $")
        all_bids.update({user_name: bid})
        other_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n")


def blind_auction():
    display_art()
    bids = {}

    get_user_bids(bids)

    max = 0
    max_bidder = ""

    for key in bids:
        user_bid = int(bids[key])
        if user_bid > max:
            max = user_bid
            max_bidder = key

    print(f"The winner is {max_bidder} with a bid of ${max}.")


blind_auction()
