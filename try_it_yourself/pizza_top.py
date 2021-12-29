# 1. Write a loop that prompts the user to enter a series of pizza toppings until they enter 'quit' value
# 2. After each value print a message saying you'll add that topping to their pizza.

# created by Bryan Chavez

prompt = "\nPlease enter pizza toppings you want"
prompt += "\n(Enter 'quit' when you are finished.) "

while True: 
    topping = input(prompt)
    if topping == 'quit':
        print("Finished making you pizza!")
        break
    else:
        print(f"Adding {topping.title()}.")
