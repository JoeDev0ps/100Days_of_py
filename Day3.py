# # TASK ONE - Rollercoaster height requirements
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# if height >= 120:
#     print("Have fun on the ride!")
# else:
#     print("Sorry, come back when you're the approved height")




# # TASK TWO - even or odd
# number = int(input("Input a number and I'll confirm if it is even or odd... "))
# if number % 2 == 0:
#     print("Even!!!")
# else:
#     print("Hmmm.... not slytherin ay??? I mean... ODD!!!")




# # TASK THREE - Nested Rollercoaster requirements
#
# 1st Attempt
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# age = int(input("How old are you? "))
# if height >= 120:
#     if age > 18:
#         print("YOU... CAN... PASS... enjoy the ride.")
#     else:
#         print("YOU... SHALL NOT... PASS... sorry you don't meet the requirements for this ride.")
# else:
#     print("Sorry, come back when you're the approved height")
#
# # Correct
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# age = int(input("How old are you? "))
# if height >= 120:
#     if age <= 12:
#         print("Please pay £5... enjoy the rides!")
#     elif age >= 13 and age <= 18:
#         print("Please pay £7... enjoy the rides!")
#     else:
#         print("Please pay £12... enjoy the rides!")
# else:
#     print("Sorry, please come back when/if you meet the requirements for our theme park!")




# # TASK FOUR - BMI calculator... enhanced!
#
# 1st Attempt
# height = float(input("What's your height (cm)? "))
# weight = int(input("What's your weight (kg)? "))
# weight_as_int = int(weight)
# height_as_float = float(height)
# bmi = round((weight_as_int / height_as_float ** 2) * 10000, 1)
# if bmi <= 18:
#     print("Your BMI shows you are underweight... BMI: ", bmi)
# elif bmi >= 19 and bmi <= 24:
#     print("Your BMI shows you are a healthy weight... BMI: ", bmi)
# elif bmi >= 25 and bmi <= 29:
#     print("Your BMI shows you are slightly overweight... BMI: ", bmi)
# elif bmi >= 30 and bmi <= 39:
#     print("Your BMI shows you are within the obese risk class... BMI: ", bmi)
# else:
#     print("Your BMI shows you are at risk of exploding... BMI: ", bmi)
#
# Correct
# height = float(input("What's your height (cm)? "))
# weight = int(input("What's your weight (kg)? "))
# bmi = round(weight / (height ** 2), 2)
# if bmi <= 18:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi >= 19 and bmi <= 24:
#     print(f"Your BMI is {bmi}, you are a healthy weight.")
# elif bmi >= 25 and bmi <= 29:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi >= 30 and bmi <= 39:
#     print(f"Your BMI is {bmi}, you are within the obese risk-class.")
# else:
#     print(f"Your BMI is {bmi}, you are at risk of exploding.")
#
# We don't actually need the ranges >=19 and <= 24, for example. We can use <
# and the program will check as the previous statement will create the range




# # TASK FIVE - Leap year indicator attempt
#
# 1st Attempt
# year = int(input("What year is it!? "))
# if year % 4 == 0:
#     print(f"The year is {year}, which is a leap year, baby!")
# elif year % 100 == 0:
#     if year % 400 == 0:
#         print(f"The year is {year} and it's a leap yearrrr, baby!")
# else:
#         print(f"The year is {year}, which is NOT a leap year, sorry!")
#
# 2nd attempt
# year = int(input("What year is it!? "))
# if year % 4 == 0:
#     if year % 100 == 0: 
#         print(f"The year is {year}, which is NOT a leap year, sorry!!")
# elif year % 4 == 0:
#     if year % 100 == 1:
#         if year % 400 == 0:
#             print(f"The year is {year} and it's a leap yearrrr, baby!")
# else:
#     print(f"The year is {year}, which is NOT a leap year, sorry!")
#
# Correct
# year = int(input("What YEAR is it!? "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("All signs say leap Year!")
#         else:
#             print("Not a leap year, sorry!")
#     else:
#         print("Leap year, baby!")
# else:
#     print("Not a leap year... >:(")




# # TASK SIX - Rollercoaster plus photos!
#
# 1st Attempt
# bill = 0
# 
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# age = int(input("How old are you? "))
# if height >= 120:
#     if age <= 12:
#         bill = 5
#         print("Child tickets are £5.")
#     elif age >= 13 and age <= 18:
#         bill = 7
#         print("Teen tickets are £7.")
#     else:
#         bill = 12
#         print("Adult tickets are £12..")
# else:
#     print("Sorry, please come back when/if you meet the requirements for our theme park!")
# 
# photos = input("Would you like photos? Y or N ")
# if photos == "yes" or "Y" or "y" or "Yes" or "YES":
#     bill += 3
# 
# print(f"Your total is £{bill}, have a good time...")
#
# Correct
# bill = 0
#
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# age = int(input("How old are you? "))
# if height >= 120:
#     if age <= 12:
#         bill = 5
#         print("Child tickets are £5.")
#     elif age >= 13 and age <= 18:
#         bill = 7
#         print("Teen tickets are £7.")
#     elif age >= 45 and age <= 55:
#         print("Everything is going to be ok have a free ride on us!")
#     else:
#         bill = 12
#         print("Adult tickets are £12..")
#
#     photos = input("Would you like photos? Y or N ")
#     if photos == "Y":
#         bill += 3
#
#     print(f"Your total is £{bill}, have a good time...")
# else:
#     print("Sorry, please come back when/if you meet the requirements for our theme park!")




# TASK SEVEN - Pizza Order
#
# 1st Attempt
# bill = 0

# intro = input("Welcome to Joe's Plain or Pepperoni Pizzaria, can I take your order? Please select Y or N... ")
# if intro == "Y":
#     pizza_size = input("What size would you like? Small (S), Medium (M), or Large (L)? ")
#     if pizza_size == "L": 
#         bill += 25
#     elif pizza_size == "M": 
#         bill += 20
#     else:
#         bill += 15
#     pepperoni = input("Would you like Pepperoni? Yes (Y) or No (N)? ")
#     if pepperoni == "Y":
#         bill += 5
#     extra_cheese = input("Would you like to add extra cheese? Yes (Y) or No (N)? ")
#     if extra_cheese == "Y":
#         bill += 2
#     double_pizza = input("Would you like to double up on your pizza order for an extra £6? Yes (Y) or No (N)")
#     if double_pizza == "Y":
#         bill += 6
#     print(f"Thanks for your order, the bill is £{bill}, we'll have it with you within 30 minutes or Spiderman's fired...")

# else:
#     print("Then stop wasting my time!") 




# TASK EIGHT - Love Calculator
#
# 1st Attempt
print ("Welcome to the Love Calculator, where is you get a score between 40 - 50 you're made for each other!")
name1 = input("What is your name? ")
name2 = input("what's their name? ")

combined_names = name1 + name2
lower_names = combined_names.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o") 
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")




# TASK NINE - Treasure Island
# print()
# print("Welcome to Treasure Island: \nThe Curse of the Moors...")
# print()
# print("Your mission is to survive and find the treasure.")
# print()
# #
# # My Code
# direction = input("You wake up stranded, it's night time... \nTo the right there's some misty fields. You look left and there's an eery bus stop... \nWhere you like to go? \nType 'Left' or 'Right' ").lower()
# print()
# if direction == "left":
#     route = input("There's seemingly two options, walk or wait... \nDo you want to wait for a bus, or walk the road?\nType 'Wait' or 'Walk' ").lower()
#     print()
#     if route == "walk":
#     # continues game
#         hitch_hiker = input("After 10 minutes of walking, something silenty rockets passed you overhead... you see a light beam down up ahead, \nDo you go into the light or Walk further? \nType 'Light' or 'Walk' ").lower()
#         print()
#         if hitch_hiker == "light":
#         # continues game
#             decision = input("You meet 3 seemingly friendly aliens... one holds out his hand to shake, the second seems to be offering food, the third wants to show you something. \nDo you want to shake hands, eat food or be shown something? \nType 'Shake', 'Eat', or 'Show' ").lower()
#             print()
#             if decision == "shake":
#                 print("The alien is venomous, you die of a highly toxic sting. \nGame Over")
#             elif decision == "eat":
#                 print("Alien food is very tasty, however it is also highly poisonous. You die immediately after your first bite swallowed. \nGame Over")
#             else:
#             # win condition
#                 print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` | `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , |` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=.|; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,_'_.|-o;   |
# |___________________|_| ;     (#) `-.o `"=..~.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
#                 print("The Alien shows you a room full of gold, they give a chest of the stuff and drop you off home... \nYou're very confused but...")
#                 print("You Win!")
#         else:
#             print("As you plan your next move, you see something in the distance... as you looking you're flattened from behind by a drunk driver. \nGame Over.")
#     else:
#         print("You continue to wait, after 30 minutes a bus arrives... 30 middle-aged men dressed at the Village People get off and beat you to death. \nGame Over.")
# else:
#     print("The path peters out... you're walking in the mud. It gets cold, then starts to rain... you get light-headed after walking for miles. Eventually your vision darkens to a complete black stillness after what feels like hours of walking in the cold & rain... You die of hypothermia in the misty moors. \nGame Over.")