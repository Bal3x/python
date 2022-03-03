# Write program that will mark a spot with an X using nested lists


row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")
rows = int(position[0])
columns = int(position[1])

map[columns - 1][rows -1] = "X"

print(f"{row1}\n{row2}\n{row3}")
