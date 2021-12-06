# create a function that asks user how many guests need to be seated at a table
# ask user for the amount of people to be seated
rest_seating = input("How many people need to be seated? ")
rest_seating = int(rest_seating)

# if more than 8 people a little wait time is needed
if rest_seating > 8:
    print("There is going to be a little bit of a wait while we prepare your table.")
else:
    print("Please come right up the we have a table ready.")
