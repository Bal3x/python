#Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake', 'tres leches']
friend_foods = my_foods[:]                          #use the slice to keep the list separate and append to add 

my_foods.append('cannoli')
my_foods.append('Mole')
friend_foods.append('ice cream')
friend_foods.append('avocado toast')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("The first three items in the list are:")
print(my_foods[:3])

print("\nThree items from the middle of the list are:")
print(my_foods[2:5])
print(friend_foods[2:5])

print("\nThe last three items on the list are:")
print(my_foods[-3:])
print(friend_foods[-3:])
