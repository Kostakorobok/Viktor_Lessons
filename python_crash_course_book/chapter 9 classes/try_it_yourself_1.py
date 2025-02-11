# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indi-
# cating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attri-
# butes individually, and then call both methods.

# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.

class restaurant:
    """Models a restaurant"""

    def __init__ (self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name.title()}\nCuisine: {self.cuisine_type.title()}")

    def open_restraurant(self):
        print(f"{self.restaurant_name.title()} is open!")

# restaurant0 = restaurant("Up and Smoke", "American Smoke House")
# restaurant0.describe_restaurant()
              
# restaurant1 = restaurant("Chikky Chan", "Asian Fusion")

# print(restaurant1.restaurant_name)
# print(restaurant1.cuisine_type)

# restaurant1.describe_restaurant()
# restaurant1.open_restraurant()

main = True

restaurant0 = restaurant("Paradai Thai", "Thai")
restaurant1 = restaurant("Harlow", "Burger diner")
restaurant2 = restaurant("Tommy Ruff", "Fish place")

restaurant0.describe_restaurant()
restaurant0.open_restraurant()

restaurant1.describe_restaurant()
restaurant1.open_restraurant()

restaurant2.describe_restaurant()
restaurant2.open_restraurant()

# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.

class user:

    def __init__ (self, first_name, last_name, age, height):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
    
    def describe_user(self):
        print(f"User Profile:\nFirst name: {self.first_name.title()}\nLast name: {self.last_name.title()}\nAge: {self.age}\nHeight: {self.height}\n")

    def greet_user(self):
        friendly_description_height = ""
        friendly_description_age = ""

        if self.height > 179:
            friendly_description_height:str = "you long"
        else:
            friendly_description_height:str = "you short"
        
        if self.age > 30:
            friendly_description_age:str = "old fuck"
        else:
            friendly_description_age:str = "baby"
       
        print(f"Hey {self.first_name.title()} {self.last_name.title()}, {friendly_description_height} {friendly_description_age}!\n")

user0 = user("Costa", "Mathew", 33, 186)
user1 = user("Anna", "Vichitra", 30, 150)
user2 = user("Rob", "Dawg", 34, 188)
user3 = user("Twee", "Smokeshow", 29, 156)

user0.describe_user()
user0.greet_user()

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()




