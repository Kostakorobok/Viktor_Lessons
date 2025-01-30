responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain woudl you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you liek to let another person to respond? (yes/no) ")
    if repeat == "no":
        polling_active = False

print("\n--- Poll Results ---")
for i, j in responses.items():
    print(f"{i.title()} would like to climb a {j.title()}.")