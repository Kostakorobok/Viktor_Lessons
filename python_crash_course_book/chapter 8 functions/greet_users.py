

def greet_users(names):
    """Print simple greeting for each user in the list"""
    for i in names:
        msg = f"Hello, {i.title()}!"
        print(msg)

usernames = ["costa", "viktor", "anna"]

greet_users(usernames)
