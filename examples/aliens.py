# aliens.py try it yourself exercises

alien_color = 'yellow'

if 'green' in alien_color:
    print("Player sucks!")
elif 'yellow' in alien_color:
    print("Player has earned 5 points.")
elif 'red' in alien_color:
    print("Player has earned 10 points.")


#stages of life tiy exercise

age = 75
print("Stages of life:")

if age < 2:
    stage = 'a baby'
elif age >= 2 and age < 4:
    stage = 'a toddler'
elif age >= 4 and age < 13:
    stage = 'a kid'
elif age >= 13 and age < 20:
    stage = 'a teenager'
elif age >= 20 and age < 65:
    stage = 'an adult'
else:
    stage = 'an elder'

print(f"This person is {stage}!")


#fruits
favorite_fruits = ['papaya', 'mango', 'pineapple', 'guava']

if 'papaya' in favorite_fruits:
    print("I really love papaya.")
if 'guava' in favorite_fruits:
    print("I really love guava.")
if 'apple' in favorite_fruits:
    print("I love apples.")


#simple dictionary

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

#accessing values in a dictionary 

alien_0 = {'color': 'red', 'points': 10}

new_points = alien_0['points']
print(f"You just earned {new_points} points!")


#adding new key-value pairs

alien_0 = {'color': 'red', 'points': 10}

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

#starting with an empty dictionary

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# modifying values in a dictionary

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")

# alien moving at different speeds

alien_0 = {'x_position':0, 'y_position': 25, 'speed': 'medium'}
print(f"Original x position: {alien_0['x_position']}")

    # move alien to the right 
    # determine how far to move the alien based on it current speed

if alien_0['speed'] == 'slow':
    x_increment = 1

elif alien_0['speed'] == 'medium':
    x_increment = 2

else:
    x_increment = 3

    # the new position is the old position plus the new position

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New x position: {alien_0['x_position']}")

# removing key value pairs

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)



