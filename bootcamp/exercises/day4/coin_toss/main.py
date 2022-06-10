# Virtual coin toss
import random

print("Welcome to the coin toss")
coin_toss = random.randint(0, 1)
if coin_toss == 0:
  print("Tails")
else:
  print("Heads")

