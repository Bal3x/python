# while loops 

# using while loops 
count = 1
while count <= 5:
    print(count)
    count += 1

# Letting the user choose when to quit program
prompt = "\nTell me something and I will repeat it to you."
prompt += "\nEnter 'quit' to end the program. "

message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# using a continue in a loop 

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# avoiding infinite loops need to have an exit criteria 
# x = 1
# while x <= 5:
#     print(x)
#     x += 1      #exit criteria





