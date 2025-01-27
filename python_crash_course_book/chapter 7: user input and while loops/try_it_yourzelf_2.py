# 7 - 4. Pizza Toppings

# pizza = {'toppings':[]}

# while True:
#     main_menu_choice = input("(1) View\n(2) Add\n(3) Exit\n").lower()

#     if main_menu_choice == "1" or main_menu_choice == "view":
#         for i, j in pizza.items():
#             print(f"{i.title()}:")
#             for k in j:
#                 print(f"\t{k.title()}")
    
#     elif main_menu_choice == "2" or main_menu_choice == "add":
#         while True:
#             pizza_topping = input("Enter a pizza topping or Q to quit: ").lower()
#             if pizza_topping == "q":
#                 break

#             print(f"I will add {pizza_topping} to your pizza!")
#             pizza['toppings'].append(pizza_topping)
    
#     elif main_menu_choice == "3" or main_menu_choice == "exit":
#         print("Exiting.")
#         break

#     else:
#         print(f"{main_menu_choice} is wrong entry, try again.")

# 7 - 5. Movie Tickets:

# menu_choice = ""
# total_price = 0
# customers = {}

# while True:
#     menu_choice = input("(1) View\n(2) Add Custsomer\n(3) Total\n(4) Quit\n")

#     if menu_choice == "1":
#         for i, j in customers.items():
#             print(f"Name: {i.title()}")
#             print(f"\tTicket price: ${j}")

#     if menu_choice == "2":
#         user_name = input("Enter your name:\n")
#         user_age = int(input("Enter your age:\n"))

#         if user_age <= 3:
#             ticket_price = "0"
#             # print(f"Ticket price: ${ticket_price}")
#         elif user_age <= 12:
#             ticket_price = "10"
#             # print(f"Ticket price: ${ticket_price}")
#         elif user_age > 12:
#             ticket_price = "15"
#             # print(f"Ticket price: ${ticket_price}")
#         else:
#             print("Wrong entry.")

#         customers[user_name] = str(ticket_price)

#     if menu_choice == "3":
#         total_price = 0
#         for i, j in customers.items():
#             total_price += int(j)

#         print(f"Total price of tickets: ${total_price}")

#     if menu_choice == "4":
#         print("Good bye.")
#         break

# 7 - 6. Three Exits. My 7 - 3 tasks covers it

# 7 - 7

# variable = 1

# while variable < 99999:
#     print("Donald Trump")


