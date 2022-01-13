# Build an automatic pizza order program
# 1. Based on a user's order, work out their final bill.

# Small Pizza : $15
# Medium Pizza : $ 20
# Large Pizza : $25
#   Pepperoni for Small Pizza: +$2
#   Pepperoni for Medium and Large Pizza: +$3
#   Extra cheese for any size pizza: +$1

print("Welcome to Python Pizza deliveries!")

# ask user for what pizza size they want
size = input("What Pizza size do you want? S, M or L ")
add_pepperoni = input("Do you want to add pepperoni? Y or N ")
extra_cheese = input("Do you want to add extra cheese? Y or N ")

bill = 0 

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your Total bill is ${bill}.")



    