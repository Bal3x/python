# this program will test the compatability between two people

import string


print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

# first need to change the names to lower case
combined_string = name1 + name2
combined_string.lower()

# use count to find out how many letters are in TRUE LOVE
T = combined_string.count("t")
R = combined_string.count("r")
U = combined_string.count("u")
E = combined_string.count("e")
L = combined_string.count("l")
O = combined_string.count("o")
V = combined_string.count("v")
E = combined_string.count("e")

Total_True = T + R + U + E 
Total_Love =  L + O + V + E 

Love_score = str(Total_True) + str(Total_Love)
#this could be combined with the previous line with int(str(Total_True) + str(Total_Love))
int_love_score = int(Love_score)

print(f"Your score is {Love_score}")

if (int_love_score < 10) or (int_love_score > 90):
  print(f"Your score is {Love_score}, you go together like coke and mentos.")
elif (int_love_score >= 40) and (int_love_score <= 50):
  print(f"Your score is {Love_score}, you are alright together.")
else:
  print(f"Your score is {Love_score}.")