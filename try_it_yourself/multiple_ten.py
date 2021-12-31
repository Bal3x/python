# ask user to input number and check if number is a multiple of 10.
number = input("Please enter a number : ")
number = int(number)

#check if is a multiple of ten
if number % 10 == 0:
    print(f"The number {number} is a multiple of ten.")
else:
    print(f"The number {number} is not a multiple of ten.")

