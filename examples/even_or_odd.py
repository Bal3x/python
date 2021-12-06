# a function that finds out if a number is even or odd

number = input("Enter a number and I will tell you if its even or odd :")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is an even number.")
else:
    print(f"\nThe number {number} is an odd number.")

    