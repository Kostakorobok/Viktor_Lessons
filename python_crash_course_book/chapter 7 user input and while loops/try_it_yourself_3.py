# 7 - 8. Deli.

# sandwich_orders = sandwiches = ["Club Sandwich", "BLT (Bacon, Lettuce, Tomato)", "Grilled Cheese", "Turkey and Avocado Sandwich", "Reuben Sandwich", "Italian Sub", "Chicken Caesar Wrap"]
# finished_sandwiches = []

# for i in sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     choice1 = input(f"I've finished making {i}, proceed to the next? (yes/no) ")

#     finished_sandwiches.append(current_sandwich)

#     if choice1 == "yes":
#         pass
#     if choice1 == "no":
#         break

# print(f"Here is the list of finished sandwiches:")
# for i in finished_sandwiches:
#     print(f"\t{i}")

# print("\n")

# 7 - 9. No Pastrami.

# sandwich_orders = ["Pastrami", "Club Sandwich", "Pastrami", "BLT", "Pastrami", "Grilled Cheese", "Pastrami", "Turkey and Avocado Sandwich", "Reuben Sandwich", "Italian Sub", "Chicken Caesar Wrap"]
# print("Current Sandwiches:")
# for i in sandwich_orders:
#     print(i)

# print("\nDeli is out of Pastrami!\n")

# while "Pastrami" in sandwich_orders:
#     sandwich_orders.remove("Pastrami")

# for i in sandwich_orders:
#     print(i)

# 7 - 10. Dream Vocation.

vocation_poll = {}
active = True

while active:
    user_name = input("What is your name? ")
    location = input("If you could visit one place in teh world, what would it be? ")

    vocation_poll[user_name] = location

    prompt0 = input("Ask another person? (yes/no)").lower()

    if prompt0 == "yes":
        continue
    elif prompt0 == "no":
        active = False
    else:
        print("Wrong input, try again.")

print("\nPoll results:")
for i, j in vocation_poll.items():
    print(f"{i.title()} wants to travel to {j.title()}")

print("\n")
    




