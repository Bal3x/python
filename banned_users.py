# checking whether a value is Not in a list

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

#try it yourself conditional tests

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

pizza = ['pepperoni', 'cheese', 'pineapple']
print("\nIs pizza == 'mushrooms'? I predict False.")
print('mushrooms'in pizza)

print("\nIs pizza == 'cheese'? I predict True.")
print('cheese'in pizza)     

game = 'destiny2'
print("\nIs game == 'destiny2'? I predict True.")
print(game == 'destiny2')

movies = ['the prestige', 'the mummy', 'pulp fiction']
movie = 'inception'

if movie not in movies:
    print(f"{movie.title()}, is not on my list.")

apps = ['instagram', 'facebook', 'twitter']
app = 'instagram'

if app in apps:
    print(f"Why is {app.title()} on the list?")