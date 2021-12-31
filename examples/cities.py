# Example: using a break to Exit a loop
# created by bal3x

prompt = "\nPlease enter the cities you have visited: "
prompt += "(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == 'quit' :
        break
    else:
        print(f"I'd love to visit {city.title()}")