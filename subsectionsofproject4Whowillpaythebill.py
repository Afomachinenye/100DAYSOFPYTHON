# Split string method

import random

names_string = input("Give me everybody's names, separated by a comma. ")

names = names_string.split(",")

num_items = len(names)

random_choice = random.randint(0, num_items-1)

The_man_who_will_pay_the_bill= names[random_choice]

print (The_man_who_will_pay_the_bill + "is going to buy the meal today")

