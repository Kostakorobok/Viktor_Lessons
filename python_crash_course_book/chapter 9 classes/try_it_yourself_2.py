# class Restaurant:
#     """Models a restaurant"""

#     def __init__ (self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
    
#     def describe_restaurant(self):
#         print(f"Restaurant name: {self.restaurant_name.title()}\nCuisine: {self.cuisine_type.title()}")

#     def open_restraurant(self):
#         print(f"{self.restaurant_name.title()} is open!")

#     def increment_number_served(self, inc_value):
#         """Increments number of customers served."""
#         self.number_served += inc_value

# restaurant = Restaurant("Up in SMoke", "BBQ Smokehouse")

# restaurant.describe_restaurant()
# print(f"{restaurant.restaurant_name.title()} served {restaurant.number_served}")

# restaurant.number_served = 20
# print(f"{restaurant.restaurant_name.title()} served {restaurant.number_served}")

# restaurant.increment_number_served(100)
# print(f"{restaurant.restaurant_name.title()} served {restaurant.number_served}")

#9-5. Login Attempts:
class user:

    def __init__ (self, first_name, last_name, age, height, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.login_attempts = login_attempts
    
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

    def increment_login_attempts(self):
        """Increments login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the number of login attempts."""
        self.login_attempts = 0

user0 = user("Costa", "Mathew", 33, 186, 0)

user0.describe_user()
print(f"{user0.first_name.title()} attempted to log in {user0.login_attempts} times")

user0.increment_login_attempts(), user0.increment_login_attempts(), user0.increment_login_attempts(), user0.increment_login_attempts()

print(f"{user0.first_name.title()} attempted to log in {user0.login_attempts} times")
user0.reset_login_attempts()

print(f"{user0.first_name.title()} attempted to log in {user0.login_attempts} times")
