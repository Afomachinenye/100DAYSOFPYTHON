# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is the ladys name name? \n")
name2 = input("What is the mans name? \n")

strin_name = (name1 + name2)
string_name = strin_name.lower()

t = string_name.count("t")
r = string_name.count("r")
u = string_name.count("u")
e = string_name.count("e")

l = string_name.count("l")
o = string_name.count("o")
v = string_name.count("v")
e = string_name.count("e")

love_score = int(str(t + r + u + e) + str( l + o + v + e))

if  (love_score < 10) or (love_score > 90):
   print (f"Your love_score is {love_score}, you go together like coke and menthol")
elif (love_score >=40) and (love_score <=50):
  print (f"Your love_score is {love_score}, you are alright together")
else:
  print (f"Your love_score is {love_score}")



