#using range() function

for value in range(1, 6):
    print(value)

numbers =  list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

#squares ** = exponents
#short version
squares = []
for value in range(1, 11):
    squares.append(value**2)
    
print(squares)

#long version
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
    
print(squares)

#using list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)

#Try It Yourself exercise 4-3
#counting to 20
twenty = []
for number in range(1, 21):
    twenty.append(number)

print(twenty)

twenty = [number for number in range(1,21)]
print(twenty)

#TIY exercise 4-6
odd_number = []
for number in range(1, 20, 2):
    odd_number.append(number)

print(odd_number)

#using list comprehension
odd_number = [number for number in range(1, 20, 2)]
print(odd_number)
