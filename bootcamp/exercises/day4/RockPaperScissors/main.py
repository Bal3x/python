# make a rock paper scissors game
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_choice >= 3 or player_choice < 0 :
  print("You typed an invalid number please try again")
else:
  computer_choice =  random.randint(0,1)

  print("Player's choice is: ")
  print(game_images[player_choice])

  print("Computer's choice is: ")
  print(game_images[computer_choice])

  if player_choice >= 3 or player_choice < 0 :
    print("You typed an invalid number please try again")
  elif player_choice == 0  and computer_choice == 2:
    print("You Win!")
  elif computer_choice == 0 and player_choice ==2:
    print("You Lose!")
  elif computer_choice > player_choice:
    print("You Lose!")
  elif player_choice > computer_choice:
    print("You Win!")
  elif computer_choice == player_choice:
    print("Its a Draw")  