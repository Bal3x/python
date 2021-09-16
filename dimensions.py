#defining a Tuple

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

#writing over a tuple

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)    

#Try it yourself exercise

buffet = ('chicken', 'waffles','beef wellington', 'onion soup', 'pizza')
print("\nThis restaurant offers the following buffet items:")
for food in buffet:
    print(food)
buffet = ('chicken', 'waffles','beef wellington', 'onion soup', 'pizza')
print("\nThis restaurant offers the following buffet items:")
for food in buffet:
    print(food)
#force error to confirm tuple can't be changed
#buffet[-1] = 'pasta'


#change item on menu
buffet = ('Pancakes', 'waffles','beef wellington', 'onion soup', 'pizza')
print("\nThis restaurant offers the following buffet items(new menu):")
for food in buffet:
    print(food)