# 6-1 person

person = {'first_name': 'carla', 'last_name': 'dones', 'age': 28, 'city': 'new york',}

print(person['first_name'].title())
print(person['last_name'].title())
print(person['age'])
print(person['city'].title())

# people's favorite numbers

favorite_numbers = {
    'jazmine': 8,
    'john': 1,
    'isabel': 5,
    'ramon': 7,
    'leticia': 9,
    }

number1 = favorite_numbers['jazmine']
number2 = favorite_numbers['john']
number3 = favorite_numbers['isabel']
number4 = favorite_numbers['ramon']
number5 = favorite_numbers['leticia']

print(f"Jazmine's favorite number is {number1}")
print(f"John's favorite number is {number2}")
print(f"Isabel's favorite number is {number3}")
print(f"Ramon's favorite number is {number4}")
print(f"Leticia's favorite number is {number5}")

# programming words learned

glosary = {
    'dictionaries': 'Storing key pairs that allow you to connect pieces.',
    'if_statements': 'Allows you to examine the current state of a program and respond appropriately.',
    'lists': 'Allow you to store sets of information in one place.',
    }

word1  = glosary['dictionaries']
word2 = glosary['if_statements']
word3 = glosary['lists']


print(f"Dictionaries: \n{word1}")
print(f"If Statements: \n{word2}")
print(f"List: \n{word3}")

# looping through a glossary 
glosary = {
    'dictionaries': 'Storing key pairs that allow you to connect pieces.',
    'if_statements': 'Allows you to examine the current state of a program and respond appropriately.',
    'lists': 'Allow you to store sets of information in one place.',
    'for loops': 'Allow you to loop through data to test conditions.', 
    'key' : 'part of the key-value dictionary.',
    'value': 'value that matches the key in a dictionary.',

    }

print("This are the key items in the glossary:")

for key in glosary.keys():
    print(key.title())

print("\nThis is the value items in the glossary:")

for value in glosary.values():
    print(value.title())

# rivers example using items()

rivers = {
    'nile': 'egypt',
    'rio grande': 'mexico',
    'rio piedras': 'puerto rico',
    'missisippi': 'united states',
    
    }

for river, country in rivers.items():
    print(f"The river {river.title()} runs through {country.title()}.")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())


# polling 

favorite_languages = {
    'jen': 'python',
    'sarah': 'c#', 
    'edward': 'ruby', 
    'phil': 'python',
    'michael': 'java', 
    'pichael': 'html', 
    'aurora': 'c++', 
    }

poll_takers = ['jen', 'sarah', 'edward', 'phil', 'aurora']

for name in favorite_languages.keys():

    if name in poll_takers:
        language = favorite_languages[name].title()
        print(f"{name.title()} thanks for taking the poll.")
    else:
        print(f"{name.title()} please take the poll.")



# Try it yourself 6-7 

people = {
    'carla': {
        'first_name': 'carla', 
        'last_name': 'dones', 
        'age': 28, 
        'city': 'new york',
        },
    'jenny': {
        'first_name': 'jenny',
        'last_name': 'cueto',
        'age': 29, 
        'city': 'new york',
        },
    'glory': {
        'first_name': 'glorilianette',
        'last_name': 'roldan',
        'age': 30,
        'city': 'san juan',
        },
    }

for name, person_info in people.items():
    
    full_name = f"{person_info['first_name']} {person_info['last_name']}"
    person_age = f"{person_info['age']}"
    person_city = f"{person_info['city']}"

    print(f"Name: {full_name.title()}")
    print(f"\tAge: {person_age.title()}")
    print(f"\tLocation: {person_city.title()}")

# list of dictionaries 6-8 pets

pet_one = {
    'animal': 'anaconda',
    'owner': 'mike',
    }
pet_two = {
    'animal': 'bat',
    'owner': 'grace',
    }
pet_three = {
    'animal': 'pig',
    'owner': 'jason',
    }

pets = [pet_one, pet_two, pet_three]

for pet in pets:
    print(pet)


# favorite places 6-9

favorite_places = {
    'ivan': ['vienna'],
    'jacob': ['madrid', 'warsaw', 'venice'],
    'lisa': ['chicago', 'paris'],
    'kyle': ['mexico city'],
    'pedro': [],
    }

for name, places in favorite_places.items():
    if len(places) == 1:
        print(f"{name.title()}'s favorite place is: ")
    elif len(places) > 1:
        print(f"{name.title()}'s favorite places are: ")
    else:
        print(f"{name.title()} tell us what your favorite places are.")
    
    for place in places:
        print(f"{place.title()}")
    
    
# exercise 6-9 favorite numbers

favorite_numbers = {
    'jazmine': [8, 3],
    'john': [1],
    'isabel': [5, 4],
    'ramon': [7],
    'leticia':[],
    }
for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(f"{name.title()}'s favorite number is: ")
    elif len(numbers) > 1:
        print(f"{name.title()}'s favorite numbers are: ")
    else:
        print(f"{name.title()} please tell us your favorite numbers.")
    
    for number in numbers:
        print(f"\t{number}")


# cities exercise 

cities = {
    'paris': {
        'country': 'france',
        'population': 'five million',
        'fact': 'eifel tower is located in Paris.'
        } ,
    'new york': {
        'country': 'usa',
        'population': 'eight million',
        'fact': 'city that never sleeps',
        }, 
    'austin': {
        'country': 'usa',
        'population': 'one million',
        'fact': 'music city',
        },
    }

for city, city_info in cities.items():
    print(f"{city.title()}:") 
    print(f"\tCountry: {city_info['country'].title()}")
    print(f"\tPopulation: {city_info['population'].title()}")
    print(f"\tFact: {city_info['fact'].title()}")
    
