# create a program that charges different ticket prices depending on the age of the person
# 1. If person is under the age of 3, ticket is free
# 2. If person is between 3 and 12, the ticket is $10
# 3. If person is over the age of 12, ticket is $15
# 4. Write a loop in which you ask the user their age and then tell them the cost of their movie ticket 

# created by Bryan Chavez

prompt = "\nPlease enter your age to determine your ticket price: "

#variable active
active = True

#while loop to test conditions
price = 0
while active: 
    print(prompt)
    age = int(input())
    if age == 0:
        print("Thank you for your payment!")
        active = False
    elif age < 3:
        price += 0
    elif age >= 3:
        price += 10
        if age > 12:
            price += 15
    print(f"The price for your admission is ${price}")
    print("(Enter '0' to pay your ticket when you are done)")
    

        

