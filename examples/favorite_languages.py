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







