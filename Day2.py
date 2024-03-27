# Tip Calculator
# FIRST ATTEMPT:
#
# def tip_calc():
#     bill = int(input("What was the bill total? "))
#     tip = bill * 0.20
#     total_amount = bill + tip
#     print("This was the tip amount: " + tip)
#     print("This was the final amount + tip: " + total_amount)
# tip_calc()

# Sub-scripting, prints 'H'
# print("Hello"[0])
# prints 'o'
# print("Hello"[-1])

# variable = "Abbey Road"
# print(variable[4] + variable[7])
# prints 'yo'

# instead of commas 
# i.e, '123,456,789' 
# we use underscores
# i.e, '123_456_789'
# python can interpret this as a whole number
# print(100_000_000) prints '100000000'

# Boolean only uses capitlised 'True' or 'False'

# len() doesn't work with integers

# if you try to concatenate a string with an integer
# this will cause a type error

# num_char = len(input("What's your name? "))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters")
# here we convert the number of num_char 
# into a string to concatenate it within print

# print(70 + float("100"))
# prints '170'
# print(str(70) + str(100))
# prints '70100'

# using type() will confirm the type of variable you're using.

# My attempt @ being stupid
# Trying to convert a string to int and adding them...
# add_nums = input("What number shall we add? ")
# new_nums = int(add_nums)
# total_nums = new_nums[0] + new_nums[1]
# print(total_nums)

#PEDMAS
# Parentheses
# Exponents
# Divison
# Multiplication
# Addition
# Subtraction

# wrong bmi cal
# height = input()
# weight = input()
# bmi = (int(weight) / float(height ** 2))
# print("Here's your shit: ", bmi)

# BMI correct
height = input("What's your height? ")
weight = input("What's your weight? ")
weight_as_int = int(weight)
height_as_float = float(height)
bmi = weight_as_int / height_as_float ** 2 
print("Your BMI is... ", bmi)

# both round to 2 decimal places
# print(round(8 / 3, 2))
# print(round(2.666666, 2))

# floor division, truncates like int() function
# print(8 // 3)
# prints '2'

# manipulating variables with arithmetic operators
# result = 4 / 2
# result /= 2
# print(result)
# prints '1.0'

# Increment variables
# score = 9
# score += 1
# print(score)
# prints '10'

# Format Strings - f strings
# score = 0
# height = 1.8
# isWinning = True
# print(f"Your Score is {score}, your height is {height} and you are winning is: {isWinning}")

# Age in weeks attempt
# age = input("What's your age? ")
# weeks_left = int(age * 52) - 4680
# print(f"You have ", {weeks_left}, " weeks left alive... TIK TOK")
# Got a huge number back... why??

# Age in weeks correct
# age = input()
# years = 90 - int(age)
# weeks = years * 52
# print(f"You have {weeks} left")

## TIP CALCULATOR 2nd ATTEMPT - still wrong
# bill = float(input("What was the bill total? "))
# tip = int(input("What tip? 10, 12 15 percent? "))
# how_many_people = int(input("How many people for this bill? "))
# bill_and_tip = bill * (tip / 100)
# per_person = float(bill_and_tip) / float(how_many_people)
# print("The per person total is £", per_person)
# for 200, 15 & 4 it gave £7.5... why??

#Bill amouint
#Tip increase
#Divide by number of people

# # TIP CALC Correct
# print("Welcome to the tip calculator!")
# bill = float(input("What was the bill total? "))
# tip = int(input("What tip? 10, 12 15 percent? "))
# how_many_people = int(input("How many people for this bill? "))
# bill_and_tip = bill * (1 + tip / 100)
# per_person = bill_and_tip / how_many_people
# final_amount = round(per_person, 2)
# # In case of £30.60p being formatted as £30.6 we use the format() method
# final_amount = "{:.2f}".format(per_person)
# print(f"The per person total is £ {final_amount}")

# # Tip Calc 2nd Attempt
# print("Welcome to the calculator take 2...")
# bill = float(input("What's the bill? "))
# people = int(input("How many people are splitting the bill? "))
# tip = int(input("What percent % tip would you like to give? "))
# total = (bill / people) * (tip / 100 + 1)
# print("Here's the total £", "{:.2f}".format(total))

# # 2nd Attempt /w comments
# print("Welcome to the calculator take 2...")
# bill = float(input("What's the bill? "))
# people = int(input("How many people are splitting the bill? "))
# tip = int(input("What percent % tip would you like to give? "))
# total = (bill / people) * (tip / 100 + 1)
# # Could also do tip / 100 * bill + bill, then divide by people
# # Same with bill * (1 + tip / 100) / (tip /100 + 1)
# print("Here's the total £", "{:.2f}".format(total))
# # don't need round if we use {:.2f}.format()
# # could also use string concatenation if we use string() type conversion on 'total'