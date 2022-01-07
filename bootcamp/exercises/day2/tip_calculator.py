# create a program that splits the bill and calculates the tip depending on the percentage selected by the user
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")

bill_amount = float(input("What is the amount of the bill?\n"))
tip = int(input("How much percentage would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people are going to split the bill?\n"))

# defined a function to truncate the decimals and select the decimal places instead of round() function
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n*multiplier)/multiplier

tip_amount = bill_amount * (tip / 100)
total_bill = bill_amount + tip_amount
bill_per_person = total_bill / people 

final_amount = truncate(bill_per_person, 2)
# needed to use .format to have 2 decimal places 
final_amount = "{:.2f}".format(bill_per_person) 

print(f"Each person should pay: ${final_amount}")




