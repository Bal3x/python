import pandas as pd

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2],
    'price' : [89000, 92000, 45000],
}
myvar = pd.DataFrame(mydataset)
print(myvar)

#create labels
a = [1, 7, 2]       #list

myVariable = pd.Series(a, index = ["x", "y", "z"])
print(myVariable)

#key/value objects as Series
calories = {"day1": 420, "day2": 380, "day3": 390}     
#dictionary keys become the labels 
myVar2 = pd.Series(calories)
print(myVar2)

#example: create a series using only data from day1 and day2
calories = {"day1": 420, "day2": 380, "day3": 390} 
myVar3 = pd.Series(calories, index = ["day1", "day2"])
print(myVar3)