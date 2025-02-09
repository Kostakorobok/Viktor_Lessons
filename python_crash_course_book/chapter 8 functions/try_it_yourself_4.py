# # 8-12. Sandwiches.

# def sandwich(sandwich):
#     print("\nYour order:")
#     for i, j in sandwich.items():
#         print(f"{i.title()}, contains:")
#         for k in j:
#             print(f"\t- {k.title()}")
#     print("\n")

# user_input = ""

# user_sandwiches = {}
# sandwich_ingredients = []

# main = True

# while main:
#     print("We will be creating a list of sandwichs and ingredients")
#     user_input = input("(1) Enter a sandwich\n(2) View existing sandwiches\n(3) Exit\n")
#     if user_input == "1":
#         sandwich_ingredients = [] 
#         sandwich_name = input("\nEnter the name of the sanwich: ").lower()
#         while user_input != "f":   
#             user_input = input("Enter an ingredient or (F) to finish: ").lower()
#             if user_input == "f":
#                 continue
#             sandwich_ingredients.append(user_input)

#         user_sandwiches[sandwich_name] = sandwich_ingredients

#     elif user_input == "2":
#         sandwich(user_sandwiches)
    
#     elif user_input == "3":
#         print("Good bye.")
#         main = False
    
#     else:
#         print("Wrong input, try again")

# # 8-13. User profiles

# def build_profile(first, last, **user_info):
#     """Build dictionary containing everything we know about the user"""
#     user_info["first name"] = first
#     user_info["last name"] = last
#     return user_info

# def add_to_profile(profile, key, value):
#     profile[key] = value

# main = True
# user_input = ""

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")

# user0 = build_profile(first_name, last_name)

# print(f"Welcome {user0["first name"].title()} {user0["last name"].title()}")

# while main:
#     print("Add something about yourself or quit.")
#     user_input = input("(1) Add data\n(2) View profile\n(3) Quit\n")
#     if user_input == "1":
#         property = input("Enter property name for the profile: ")
#         description = input("Enter the value of the property: ")

#         add_to_profile(user0, property, description)

#     elif user_input == "2":
#         for i, j in user0.items():
#             print(f"{i.title()}: {j.title()}")
    
#     elif user_input == "3":
#         print(f"Good bye {user0["first name"].title()} {user0["last name"].title()}")
#         main = False

#     else:
#         print("Wrong input, try again")

# 8-14. Cars: Write a function that stores information about a car in a diction-
# ary. The function should always receive a manufacturer and a model name. It
# should then accept an arbitrary number of keyword arguments. Call the func-
# tion with the required information and two other name-value pairs, such as a
# color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was
# stored correctly.

def make_car(manufacturer, model, **car_properties):
    car_properties["manufacturer"] = manufacturer
    car_properties["model"] = model
    return car_properties

car0 = {}
car0 = make_car("honda", "accord", color = "grey", year = "2012", service = True)

for i, j in car0.items():
    print(f"{i.title()}: {j}")
    

