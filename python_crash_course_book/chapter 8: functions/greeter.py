def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

user0 = input("Enter your name: \n")
greet_user(user0)
