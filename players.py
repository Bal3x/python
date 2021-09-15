#slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

#if first index is omitted python starts at the beginning of the list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

#if you want the end of the list you omit the last index
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])

#if we want the last three players we can use 
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

#looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

