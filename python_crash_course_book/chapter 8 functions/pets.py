# def describe_pet(animal_type, animal_name):
#     """Display Information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {animal_name.title()}.")

# have_pet = True

# while have_pet:
#     pet_type = input("\nEnter the type of your pet (cat, dog, etc.)")
#     pet_name = input("Enter your pet's name: ")

#     describe_pet(pet_type, pet_name)

#     choice0 = input("\nDo you have another pet?\n yes/no\n")
#     if choice0 == "yes":
#         continue
#     else:
#         have_pet = False

# def describe_pet(animal_type, animal_name):
#     """Display Information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {animal_name.title()}.")

# describe_pet(animal_type = "Dog", animal_name = "Huxley")

def describe_pet(animal_name, animal_type = "dog"):
    """Display Information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {animal_name.title()}.")

describe_pet("Lucky", "Cat")


