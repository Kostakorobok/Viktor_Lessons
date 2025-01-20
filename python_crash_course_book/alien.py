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

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}\n")
speed_choice = True

while(speed_choice):
    alien_speed = str(input(f"What is the speed of the alien?\n| Slow | Medium | Fast |\n")).lower()
    if alien_speed == 'slow':
        alien_0['speed'] == 'slow'
        x_increment = 1
        speed_choice = False
    elif alien_speed == 'medium':
        alien_0['speed'] == 'medium' 
        x_increment = 2
        speed_choice = False
    elif alien_speed == 'fast':
        alien_0['speed'] == 'fast'
        x_increment = 3
        speed_choice = False
    else:
        print('Wrong input, try again.\n')

alien_0['speed'] = alien_speed

alien_0['x_position'] += x_increment

print(f"New position: {alien_0['x_position']}")


