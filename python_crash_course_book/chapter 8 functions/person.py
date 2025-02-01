
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {"first name": first_name, "last name": last_name}
    return person

musician = build_person("jimmy", "hendrix")

print(musician)

for i, j in musician.items():
    print(f"{i.title()} : {j.title()}")