# 7-1. Rental Car: Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as “Let me see if I can find you
# a Subaru.”

# car_choice = input("Enter make of a car you want: ")
# print(f"Let me see if I can find you a {car_choice}")

# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message say-
# ing they’ll have to wait for a table. Otherwise, report that their table is ready.

# no_people = int(input("How many people are in your dinner group?\n"))
# if no_people > 8:
#     print("All tables are taken, you'll have to wait")
# else:
#     print("Your table is ready")

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

user_number = int(input("Please enter a number: "))

if user_number % 10 == 0:
    print(f"{user_number} is a multiple of 10")

else:
    print(f"{user_number} is not a multiple of 10")
