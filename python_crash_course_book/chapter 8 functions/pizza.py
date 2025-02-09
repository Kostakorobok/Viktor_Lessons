# def make_pizza(*toppings):
#     ''' Print list of toppings that have been selected '''
#     print(toppings)

# # make_pizza("peperoni")
# # make_pizza("mushrooms", "peperoni", "ham")

# toppings0 = ["mushrooms", "peperoni", "ham", "bell peppers"]
# make_pizza(toppings0)

# def make_pizza(toppings):
#     ''' Print list of toppings that have been selected '''
#     print("\nThe following toppings have been ordered:")
#     for i in toppings:
#         print(f"- {i.title()}")

# list_toppings = []
# add_toppings = True

# while add_toppings:
#     menu_choice = input("(add) Add toppings\n(view) View current toppings\n(quit) Quit program\n").lower()
#     if menu_choice == "add":
#         new_topping = input("\nEnter a topping you want to add: ")
#         list_toppings.append(new_topping)
#     elif menu_choice == "view":
#         make_pizza(list_toppings)
#     elif menu_choice == "quit":
#         add_toppings = False
#     else:
#         print("Wrong input, try again")

def make_pizza(size, *toppings):
    """Summarize the pizza we about to make."""
    print(f"\nMaing a {size} pizza with the following toppings:")
    for i in toppings:
        print(f"- {i}")
    
# make_pizza(16, "pepperoni")
# make_pizza(12, "mushrooms", "green peppers", "extra cheese")



