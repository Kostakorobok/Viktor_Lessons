import random

logo = """
██████╗ ██╗      █████╗  ██████╗██╗  ██╗         ██╗ █████╗  ██████╗██╗  ██╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝         ██║██╔══██╗██╔════╝██║ ██╔╝
██████╔╝██║     ███████║██║     █████╔╝          ██║███████║██║     █████╔╝ 
██╔══██╗██║     ██╔══██║██║     ██╔═██╗     ██   ██║██╔══██║██║     ██╔═██╗ 
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗    ╚█████╔╝██║  ██║╚██████╗██║  ██╗
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝                                                                            
"""

print(logo)
deck0 = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

main = True
game_on = True

def ft_dealing_cards(deck, player):
    for i in range (2):
        card = random.choice(deck)
        player.append(card)

def ft_add_card(deck, player):
    card = random.choice(deck)
    player.append(card)
   
def ft_card_sum(player, total_count):
    total_count = 0
    for i in player:
        total_count += i
    return total_count

def rules():
    print("\nPaste rules of black jack at later date\n")

while main:
    user_cards = []
    ai_cards = []

    user_cards_total = 0 
    ai_cards_total = 0

    menu_choice = input("\n____Menu____:\n(1) Start new game\n(2) Rules\n(3) Quit\n")
    if menu_choice == "1":
        game_on = True        
        ft_dealing_cards(deck0, user_cards), ft_dealing_cards(deck0, ai_cards)

        while game_on:

            user_cards = [11, 10] # Testing code
            ai_cards = [11, 10] # Testing code

            user_cards_total = ft_card_sum(user_cards, user_cards_total) 
            ai_cards_total = ft_card_sum(ai_cards, ai_cards_total)

            print(f"\nYour cards are: {user_cards}\nTotal: {user_cards_total}")
            print(f"\nAI's cards are: {ai_cards}\nTotal: {ai_cards_total}")

            if user_cards_total == 21 and ai_cards_total != 21:
                print("Black Jack! You win!")
                game_on = False
            elif ai_cards_total == 21 and user_cards_total != 21:
                print("Black Jack! You loose, AI wins!")
                game_on = False
            elif user_cards_total == 21 and ai_cards_total == 21:
                print("Double Black Jack! Draw!")
                game_on = False
            else:  
                if user_cards_total > 21:
                    print("User score is over 21\nChecking if have Ace...\n")   
                    for i in user_cards:
                        if i == 11:
                            pass
                        else:
                            game_on = False
                            print("You loose!")       
            input("code stop")
    elif menu_choice == "2":
        rules()
    elif menu_choice == "3":
        main = False
        print("Goodbye")
    else:
        print("\nWrong input, try again.\n")




