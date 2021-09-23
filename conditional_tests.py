#more conditional tests
#test for equality

car = 'BMW'

print(car.lower() == 'bmw')

#test for inequality

food = 'Garlic bread'
print(food.lower() == 'garlic bread')

#testing with numbers
age = 21
print(age > 21)
print(age < 21)
print(age >= 21)
print(age <= 21)

#using and/or statements
grandmas_age = 86
my_age = 28
print(my_age <= 30 and grandmas_age >= 45)
print(my_age >= 30 and grandmas_age >= 100)
print(my_age > 25 or grandmas_age > 100)
print(my_age > 30 or grandmas_age > 100)


#test for item in a list
games = ['call of duty', 'destiny2', 'tomb raider', 'apex']
game = 'tomb raider'

if game in games:
    print(f"\nI love that {game.title()}!")

#test for item not in a list
movies = ['batman returns', 'pearl harbor', 'goonies']
movie = 'desperado'

if movie not in movies:
    print(f"\nI haven't seen {movie.title()}.")

