# def greet_user(username):
#     """Display a simple greeting."""
#     print(f"Hello, {username.title()}!")

# user0 = input("Enter your name: \n")
# greet_user(user0)

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nEnter your name: \n(Enter Q to quit)")
    f_name = input("First name: ").lower()
    if f_name == "q":
        break
    l_name = input("Last name: ").lower()
    if l_name == "q":
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")
