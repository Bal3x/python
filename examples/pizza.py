# storing a list on a dictionary

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese', 'pepperoni'],
    }

#summarize your order

print(f"You order a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

