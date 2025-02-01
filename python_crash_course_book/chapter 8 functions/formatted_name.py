
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name("jimmy", "hendirx")
# print(musician)

def get_formatted_name(first_name, last_name, middle_name = ""):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

a_first_name = input("Enter your first name: ")
a_middle_name = input("Enter middle name, or hit enter to continue: ")
a_last_name = input("Enter your last name: ")

musician = get_formatted_name(a_first_name, a_last_name, a_middle_name)

print(musician)
