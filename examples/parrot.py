# how the input() function works

message = input("Tell me something and I will repeat it back to you: ")
print(message)

# using clear prompts 

name = input("Please enter your name: ")
print(f"Hello {name.title()}!")

# when you want to have a longer line

prompt = "If you tell me who you are, I can personalize the messages you see."
prompt += "\nWhat is your name? "

name = input(prompt)
print(f"Hello, {name.title()}!")

jobs = input("How many jobs have you applied?: ") 

