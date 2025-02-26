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

def dev_code_stop():
    input("\npress Enter to continue\n")

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
        draw_card = True        
        ft_dealing_cards(deck0, user_cards), ft_dealing_cards(deck0, ai_cards)

        while game_on:

            # user_cards = [12, 11] # Testing code
            # ai_cards = [11, 10] # Testing code

            while draw_card:
                user_cards_total = ft_card_sum(user_cards, user_cards_total) 
                ai_cards_total = ft_card_sum(ai_cards, ai_cards_total)

                print(f"\nYour cards are: {user_cards}\nTotal: {user_cards_total}")
                print(f"\nAI's cards are: {ai_cards}\nTotal: {ai_cards_total}")

                if user_cards_total == 21 and ai_cards_total != 21:
                    print("\nBlack Jack! You win!")
                    draw_card = False
                    game_on = False
                    dev_code_stop()
                elif ai_cards_total == 21 and user_cards_total != 21:
                    print("\nBlack Jack! You loose, AI wins!")
                    draw_card = False
                    game_on = False
                elif user_cards_total == 21 and ai_cards_total == 21:
                    print("\nDouble Black Jack! Draw!")
                    draw_card = False
                    game_on = False
                else:  
                    if user_cards_total > 21:
                        print("\nUser score is over 21\nChecking if have Ace...\n")  
                        dev_code_stop()
                        for i in range(len(user_cards)):
                            if user_cards[i] == 11:
                                user_cards_total = 0
                                user_cards[i] = 1
                                print(user_cards)
                                user_cards_total = ft_card_sum(user_cards, user_cards_total)

                                if user_cards_total > 21:
                                    draw_card = False
                                    game_on = False
                                    print("\nYou have ACE but still loose!")
                                    dev_code_stop()
                                    break
                                else:
                                    user_cards[i] = 11
                                    print("\nAfter changing Value of of Ace from 11 to 1, your score is now lower than 21.\nGame carries on.")
                                    dev_code_stop()
                                break
                            else:
                                break
                            
                        if 11 not in user_cards:
                            draw_card = False
                            game_on = False
                            print("\nYou dont have an Ace. You loose!")       
                            dev_code_stop()
                            break
                
                    print(f"\nUser's curent Hand: {user_cards}")

                    draw_card_choice = input("\nDraw another card?\n yes/no\n").lower()
                    if draw_card_choice == "yes":
                        ft_add_card(deck0, user_cards)
                        print(f"\nYou drew another card. Your current hand is: {user_cards}")
                        dev_code_stop()
                    elif draw_card_choice == "no":
                        print(f"\nYou've choosen not to draw card. Your current hand is: {user_cards}")
                        print(f"AI's current hand is: {ai_cards}\nAIs term:")
                        dev_code_stop()

                        if ai_cards_total < 17:
                            print(f"AIs total score is {ai_cards_total}, which is less than 17, thus drawing another card:")
                            dev_code_stop
                            ft_add_card(deck0, ai_cards)
                            ai_cards_total = ft_card_sum(ai_cards, ai_cards_total)
                            if ai_cards_total > 21:
                                draw_card = False
                                game_on = False
                                print(f"AI's new hand: {ai_cards}\nAI's new total: {ai_cards_total}")
                                print("AI wins!")
                                dev_code_stop()
                                break
                        
                        else:
                            ai_cards_total = ft_card_sum(ai_cards, ai_cards_total)
                            print(f"User hand: {user_cards} | User score: {user_cards_total}")
                            print(f"AI's hand: {ai_cards}   | AI's score: {ai_cards_total}")

                            if ai_cards_total > user_cards_total:
                                draw_card = False
                                game_on = False
                                print("AI Wins!")
                                break
                            elif ai_cards_total < user_cards_total:
                                draw_card = False
                                game_on = False
                                print("User wins")
                                break
                            else:
                                draw_card = False
                                game_on = False
                                print("Draw!")
                                break

                    else:
                        print("\nWrong input, try again.\n")


    elif menu_choice == "2":
        rules()
    elif menu_choice == "3":
        main = False
        print("Goodbye")
    else:
        print("\nWrong input, try again.\n")




