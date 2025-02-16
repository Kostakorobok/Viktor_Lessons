# # 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# # a class called IceCreamStand that inherits from the Restaurant class you wrote
# # in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
# # the class will work; just pick the one you like better. Add an attribute called
# # flavors that stores a list of ice cream flavors. Write a method that displays
# # these flavors. Create an instance of IceCreamStand, and call this method.

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

# class Ice_Cream_Stand(Restaurant):
#     """Child class of a restaurant super-class"""
#     def __init__ (self, restaurant_name, cuisine_type, flavours):
#         self.flavours = flavours
#         """Initiates attributes of a restaurant"""
#         super().__init__(restaurant_name, cuisine_type)

#     def view_flavours(self, flavours):
#         print("This restuarant serves the following flavours of the ice-cream:")
#         for i in flavours:
#             print(f"- {i.title()}")

# stand0_flavours = ["chocolate", "vanilla", "cherry", "mango"]

# stand0 = Ice_Cream_Stand("Mordi IceCream", "Gelateria", stand0_flavours)

# stand0.describe_restaurant()
# stand0.view_flavours(stand0_flavours)

# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
# or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.

class User:

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

class Privilleges:
    def __init__ (self):
        self.privilleges = ["Can add post", "can delete post", "can ban user"]
    
    def show_privilleges(self, privilleges):
        print(f"{self.first_name.title()} {self.last_name.title()} has the following privilleges:")
        for i in privilleges:
            print(f"- {i}")

class Admin(User):
    """Creates an Admin user type"""
    def __init__ (self, first_name, last_name, age, height, login_attempts):
        """Initiates attributes of user class"""
        super().__init__(first_name, last_name, age, height, login_attempts)
        self.privilleges = Privilleges()


admin0 = Admin("Costa", "Mathew", 33, 186, 0,)   

admin0.increment_login_attempts(), admin0.increment_login_attempts(), admin0.increment_login_attempts(), admin0.increment_login_attempts()
admin0.reset_login_attempts()
admin0.increment_login_attempts()

admin0.greet_user()
print(f"Log in attempts: {admin0.login_attempts}")

# 9-8. Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.

admin0.privilleges.show_privilleges()

