import random

random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else:
  print ("Tails")


  name = input("type:")
  names =name.split(",")
  print (names)