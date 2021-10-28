# dictionary of similar objects

favorite_languages = {
    'jen': 'python',
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# looping thru all key-value pairs in a dictionary

favorite_languages = {
    'jen': 'python',
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# looping thru all the keys in a dictionary

favorite_languages = {
    'jen': 'python',
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python',
    }

for name in favorite_languages.keys():
    print(name.title())

# Favorite languages message to friends

favorite_languages = {
    'jen': 'python',
    'sarah': 'c#', 
    'edward': 'ruby', 
    'phil': 'python',
    }

friends =  ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language} too!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take the poll!")

# looping throught a dicionary's keys in a particular order 

favorite_languages = {
    'jen': 'python',
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll!")


# looping through all values in a dictionary using value() method

favorite_languages = {
    'jen': 'python',
    'sarah': 'c#', 
    'edward': 'ruby', 
    'phil': 'python',
    }
print("The following languages have been mentioned:")

for language in favorite_languages.values():
    print(language.title())

# using set to loop through values that are unique to avoid repetition on large data sets

favorite_languages = {
    'jen': 'python',
    'sarah': 'c#', 
    'edward': 'ruby', 
    'phil': 'python',
    }

print("The following languages have been mentioned:")

for language in set(favorite_languages.values()):
    print(language.title())


# looping thru a list inside a dictionary (values from single keys)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c#', 'c++'], 
    'edward': ['ruby', 'java'], 
    'phil': ['python', 'c'],
    }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    
    for language in languages:
        print(f"{language.title()}")

# same example but with places to live list inside dicitonaries 

favorite_places = {
    'kyle': ['boston', 'new york'], 
    'hanah': ['austin'], 
    'jake': ['miami', 'chicago'],
    'chris': [],
    }

for name, cities in favorite_places.items():
    
    if len(cities) == 1:
        print(f"\n{name.title()}'s favorite place to live is: ")
    elif len(cities) > 1:
        print(f"\n{name.title()}'s favorite places to live are: ")
    else:
        print(f"\n{name.title()} please tell us what city you would like to live.")

    for city in cities:
        print(f"{city.title()}")

