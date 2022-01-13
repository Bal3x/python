# # day 3 conditional operators examples

# Example 1: create a program that verifies the height of a person and decides wether or not its tall enough to ride

print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0

if height >= 120:
    print("You can ride the Rollercoaster!")
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.00.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.00.")
    else:
        bill = 12
        print("Adult tickets are $12.00.")
    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y" or "y":
        bill += 3

    print(f"Your final bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")


# # Example 2: is it odd or even?
# # Write a program that works out whether if a given number is an odd or even number
# # hint: even number can be devided by 2 with no remainder.

# number = int(input("Please enter a number and I will tell you if it's even or odd.\n"))

# if number % 2 == 0:
#     print(f"{number} is even number.")
# else:
#     print(f"{number} is odd number.") 

# # Exercise 1:
# # Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# # It should tell them the interpretation of their BMI based on the BMI value. 
# #   Under 18.5 they are underweight
# #   Over 18.5 but below 25 they have a normal weight
# #   Over 25 but below 30 they are slightly overweight
# #   Over 30 but below 35 they are obese
# #   Above 35 they are clinically obese


# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in m: "))
# bmi = round((weight)/(height**2))

# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are Underweight.")
# elif bmi <= 25:
#     print(f"Your BMI is {bmi}, you have a Normal Weight.")
# elif bmi <= 30:
#     print(f"Your BMI is {bmi}, you are Slightly Overweight.")
# elif bmi <= 35:
#     print(f"Your BMI is {bmi}, you are Obese.")
# else:
#     print(f"Your BMI is {bmi}, you are Clinically Obese.")



