# # Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# two_digit_number = input("Type a two digit number: \n")
# # get the first and second digits using subscripting then convert string to int
# # sum the first and second digits 
# print(int(two_digit_number[0]) + int(two_digit_number[1]))

# # mathematical operations
# # PENDAS
# # ()
# # ** 
# # */
# # +-

# print(3 * (3 + 3) / 3 - 3)


# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m)
# weight = input("Enter your weight in kg: ")
# height = input("Enter your height in m: ")


# bmi = (int(weight)/float(height)**2)

# bmi_int = int(bmi)
# print(bmi_int)

print(round(8/3, 2)) #round function will round the number to the decimals that I select

print(8//3) #floor function // is used when I want to maintain the same data type integer instead of a float.

result = 4/2
result /= 2             # if i want to use the previous variable to keep track of it I can use the shorcut to (mathematical operator followed by = sign)

score = 0 
score += 1         
# other example are"
#score *= 2
#score /= 3

print(score)

# f-strings
print(f"your score is {score}")


