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

# using a Flag



