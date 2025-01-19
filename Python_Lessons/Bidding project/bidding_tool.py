logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

# Find max function:
def ft_find_max(dictionary):
    max = 0
    bidder_name = ""
    for key, value in dictionary.items():
        if value > max:
            max = value
            bidder_name = key
    print(f"Name: {bidder_name}\nBid:$ {max}")

auction_active = True
no_bidders = 0

while(auction_active):
    bids = {}
    add_bidder = True

    while(add_bidder):
        print(f"Current number of bidders: {no_bidders}")
        user_choice = input("Add another bidder?\n(Y) Yes (N) No\n").lower()

        if user_choice == "y":
            no_bidders += 1
            temp_bidder_name = input(f"Bidder number {no_bidders}, enter your name:\n")
            temp_bidder_bid = int(input(f"Bidder number {no_bidders}, enter your bid:\n$ "))
            bids[temp_bidder_name] = temp_bidder_bid
            print("Bids:")
            print(bids)
            
        elif user_choice == "n":
            add_bidder = False
            auction_active = False
            print("Auction winner:")
            ft_find_max(bids)
            break
        else:
            print("Wrong input, try again\n")

