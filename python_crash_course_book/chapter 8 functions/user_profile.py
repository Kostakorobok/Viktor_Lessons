def build_profile(first, last, **user_info):
    """Build dictionary containing everything we know about the user"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_profile('albert', 'einstain', location = "princenton", field = "physics")

for i, j in user_profile.items():
    print(f"{i.title()}: {j.title()}")
