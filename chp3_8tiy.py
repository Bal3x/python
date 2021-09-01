#3.8 Seeing the world

places = ['peru', 'spain', 'morocco', 'argentina', 'japan']
print("Here is the original list:")
print(places)

print("\nHere is the sorted list in alphabetical order:")
print(sorted(places))

print("\nHere is the original list again:")
print(places)

print("\nHere is the list in reverse alphabetical order:")
print(sorted(places, reverse=True))

print("\nHere is the list using reverse():")
places.reverse()
print(places)

print("\nHere is list reversed to its original:")
places.reverse()
print(places)

print("\nHere is the list sorted using the sort() method:")
places.sort()
print(places)

print("\nHere is the list in reversed alphabetical order:")
places.sort(reverse=True)
print(places)


