# Write a program which will select a random name from a list of names. 
import random

# Split string method 

names_string = input("Give me everybody's names, separated by a comma.")
names = names_string.split(", ")
random_choice = random.randint(0, len(names) - 1)

print(f"The person selected at random is {names[random_choice]}.")

#using .choice()
random_choice = random.choice(names)
print(f"The person selected at random using random.choice() is {random_choice}.")