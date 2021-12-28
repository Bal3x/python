# Letting the user quit the program
# Created by bal3x

prompt = "\nTell me anything and I will repeated to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""

# while message != 'quit':
#     message = input(prompt)
    
#     if message != 'quit':
#         print(message)


# using a flag to determine when to stop a program
active = True
while active : 
    message = input(prompt)
    if message == 'quit' :
        active = False
    else:
        print(message)


