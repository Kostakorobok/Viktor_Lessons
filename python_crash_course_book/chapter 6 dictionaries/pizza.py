# pizza toppings

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print(f"You've ordered {pizza['crust']} pizza with the following toppings:")
for i in pizza['toppings']:
    print("\t" + i)

