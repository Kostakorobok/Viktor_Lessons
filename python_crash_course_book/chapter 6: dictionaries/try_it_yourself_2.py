# 6-4. Glossary 2:
# 6-3. Glossary
print("Task 6 - 3:")
python_glossary = {
    'print()': 'this function allows you to display outputs onto the terminal.',
    'list': 'this function stores list or lists of items.',
    'boolean variable = True or False': 'creates  a bool that can be either true or false. True or False must have capital letter.'
}

for key, value in python_glossary.items():
    print(f"\n- {key}: {value}")

# 6-5. Rivers:
print("Task 6 - 5:")
rivers = {
     'nile': 'egypt',
     'tames': 'england',
     'neman': 'belarus'
 }

for river, city in rivers.items():
    print(f"{river.title()} runs through {city.title()}.")

for river in rivers.keys():
    print(river)

for city in rivers.values():
    print(city)

# 6-6. Polling:
