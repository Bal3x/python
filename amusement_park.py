# if - elif - else chain example

age = 12

if age < 4:
    print("Your admission cost is $0.")

elif age < 18:
    print("Your admission cost is $25.")

else:
    print("Your admission cost is $40.")

#below - more concise better programming (if the print needs to be changed then it will only take one change instead of three.)

age = 90

if age < 4:
    price = 0

elif age < 18:
    price = 25

elif age < 65:
    price = 40

elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")