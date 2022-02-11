#rock, scissors, paper 

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

my_choice = int(input("What do you choose: Tye 0 for Rock, 1 for Paper or 2 for scissors:\n"))
if my_choice >=3 or my_choice <0:
  print ("You typed an invalid number, you loose")
else:   
    print(game_images[my_choice])

computer_choice = random.randint(0, 2)
print (game_images[computer_choice])

print (f"Computer chose {computer_choice}")

if my_choice == 0 and computer_choice == 2:
  print("You win!")

elif my_choice >=3 or my_choice <0:
  print ("You typed an invalid number, you loose")

elif computer_choice > my_choice:
     print ("You loose!")

elif computer_choice == my_choice:
    print ("It\"s a draw")

elif my_choice == 2 and computer_choice == 0:
  print("You loose")

elif my_choice > computer_choice:
  print("You win")






