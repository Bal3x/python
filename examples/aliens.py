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
