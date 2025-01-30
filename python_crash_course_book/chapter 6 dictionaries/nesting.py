# nesting:

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# creating fleet of aliens:

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print(f"Total number of aliens created: {len(aliens)}")

for i in aliens[:3]:
    if i['color'] == 'green':
        i['color'] = 'yellow'
        i['points'] = 10
        i['speed'] = 'medium'


for  i in aliens:
    if i['color'] == 'yellow':
        i['color'] = 'red'
        i['points'] = 15
        i['speed'] = 'fast'
    elif i['color'] == 'green':
        i['color'] = 'yellow'
        i['points'] = 10
        i['speed'] = 'medium'

for i in aliens:
    print(i)


