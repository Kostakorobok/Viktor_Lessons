# 8-3. T-shirt:

# def make_tshirt(size, print_text):
#     print(f"T-shirt:\nSize: {size}\nPrint: {print_text}")

# user_size = input("Enter the size of the T-shirt:\n")
# user_print = input("Enter the print on the T-shirt:\n")

# make_tshirt(user_size, user_print)
# make_tshirt(print_text = "Front Runner", size = "Small")

# 8-4. Large Shirts

# def make_tshirt(print_text, size = "Large"):
#     print(f"T-shirt:\nSize: {size}\nPrint: {print_text}")

# make_tshirt("I love Python")

# 8-5. Cities

def describe_city(city, country):
    print(f"{city} is in {country}")

user_city = input("Enter a city: ")
user_country = input(f"What country is {user_city} located in: ")

describe_city(user_city, user_country)
describe_city(country = "Ukraine", city = "Kiev")
describe_city("London", country = "England")


