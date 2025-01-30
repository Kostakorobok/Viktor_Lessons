# Chapter 6 examples:

# alien_0 = {'color': 'green', 'points': 5}

# print(alien_0['color'])
# print(alien_0['points'])

# new_points = alien_0['points']
# print(f"You've earned {new_points} points!")

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# alien_0 = {}
# print(alien_0)

# alien_0['color'] = 'green'
# print(alien_0)
# alien_0['points'] = 5
# print(alien_0)
# print(f"The alien is {alien_0['color']}")

# alien_0['color'] = input("What is the new colour of the alien?\n")
# print(f"New color of the alien is {alien_0['color']}!")

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original position: {alien_0['x_position']}\n")
# speed_choice = True

# while(speed_choice):
#     alien_speed = str(input(f"What is the speed of the alien?\n| Slow | Medium | Fast |\n")).lower()
#     if alien_speed == 'slow':
#         alien_0['speed'] == 'slow'
#         x_increment = 1
#         speed_choice = False
#     elif alien_speed == 'medium':
#         alien_0['speed'] == 'medium' 
#         x_increment = 2
#         speed_choice = False
#     elif alien_speed == 'fast':
#         alien_0['speed'] == 'fast'
#         x_increment = 3
#         speed_choice = False
#     else:
#         print('Wrong input, try again.\n')

# alien_0['speed'] = alien_speed

# alien_0['x_position'] += x_increment

# print(f"New position: {alien_0['x_position']}")

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# del alien_0['points']
# print( alien_0)

friends = ['phil', 'sarah']

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    # 'erin': 'ruby'
}

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language[0].title()} and {language[1].title()}.")

for name in favorite_languages.keys():
    print(f"Hi {name.title()}!")
    if name in friends:
        language = favorite_languages[name]
        print(f"\t{name.title()}, I see you love {language.title()}!")

if 'erin' not in favorite_languages.keys():
    print('\nErin, take your poll!\n')

for language in set(favorite_languages.values()):
    print(language.title())

# print(favorite_languages['sarah'])

# alien_0 = {'color': 'green', 'speed': 'slow'}
# # print(alien_0['points'])

# point_value = alien_0.get('points', 'No point value assigned.')
# print(point_value)

#try it yourself
# # 6-1. Person

# person_0 = {
#     'first name': 'Donald',
#     'last name': 'Trump',
#     'age': 78,
#     'city': 'Capitol'
# }

# print(f"Person stored in person_0 is {person_0['first name']} {person_0['last name']}, he is {person_0['age']} years old and lives in {person_0['city']}.")

# # 6-2. Favorite numbers
# favorite_numbers = {
#     'Costa': 88,
#     'Karn': 69,
#     'Phil': 125,
#     'Raji': 3,
#     'Warren': 3
# }
# print(f'Costas favorite number is {favorite_numbers['Costa']}\nKarns favorite number is {favorite_numbers['Karn']}\nPhils favorite number {favorite_numbers['Phil']}\nRajis favorite {favorite_numbers['Raji']}\nWarrens favorite number {favorite_numbers['Warren']}\n')

# # 6-3. Glossary
# python_glossary = {
#     'print()': 'this function allows you to display outputs onto the terminal.',
#     'list': 'this function stores list or lists of items.',
#     'boolean variable = True or False': 'creates  a bool that can be either true or false. True or False must have capital letter.'
# }

# for i in python_glossary.keys():
#     print(f'{i}:\n{python_glossary[i]}\n')

# looping through a dictionary

# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi'
# }

# for key, value in user_0.items():
#     print(f'\nKey: {key}')
#     print(f'Value: {value}')



