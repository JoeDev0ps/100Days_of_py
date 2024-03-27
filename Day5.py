## EXAMPLE LOOP
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
# print(fruits)




## TASK ONE - Create a height average calculator
## My attempt
# # Input a Python list of student heights
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
#
# # Write your code below this row 👇
# total_height = 0
# for student in student_heights:
#   total_height += student_heights[n]
#
# print("Average classroom height:", total_height / len(student_heights))
# print("Total classroom height:", total_height)
# print("Number of studnets =", len(student_heights))
#
# Tutor answer
#
# # Input a Python list of student heights
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # Your code below this row 👇
# total_height = 0
# for height in student_heights:
#   total_height += height
# print(f"total height = {total_height}")
#
# number_of_students = 0
# for student in student_heights:
#   number_of_students += 1
# print(f"number of students = {number_of_students}")




## TASK TWO - Print highest score
# # Input a list of student scores
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])

# # Write your code below this row 👇
# highest_score = 0
# for score in student_scores:
#   if score > highest_score:
#     highest_score = score

# print("The highest score today is,", highest_score)




## TASK THREE - Adding even numbers
# For Loop with Range
# for number in range(1, 11, 3):
#   print(number)
# prints numbers from 1 to 11 in 3 steps, i.e, 1, 4, 7, 10
#
# My Attempt
# 
# target = int(input()) # Enter a number between 0 and 1000
# # 🚨 Do not change the code above ☝️
#
# # Write your code here 👇
# target_number = 0
# for number in range(2, target + 2, 2):
#   target_number += number
#
# print(target_number)
#
# Alternate method
#
# alternative_sum = 0
# for number in range(1, target + 1):
#   if number % 2 == 0:
#     alternative_sum += number
# print(alternative_sum)




# TASK FOUR - FizzBuzz
#
# My Attempt 1
#
# Write your code here 👇
# for n in range(100):
#   if n == 0:
#     print(n)
#   elif n % 3 == 0 and n % 5 == 0:
#     print("FizzBuzz")
#   elif n % 3 == 0:
#     print("Fizz")
#   elif n % 5 == 0:
#     print("Buzz")
#   else:
#     print(n)
# Only printed upto 99, 0 printed Fizz for some reason
#
# My Attempt 2
#
# Write your code here 👇
# target = 100
# for n in range(1, target + 1):
#   if n == 0:
#     print(n)
#   elif n % 3 == 0 and n % 5 == 0:
#     print("FizzBuzz")
#   elif n % 3 == 0:
#     print("Fizz")
#   elif n % 5 == 0:
#     print("Buzz")
#   else:
#     print(n)




# TASK SIX - Paswword Generator
#
# Hard level
#
# First attempt
# password = []
# for letters in nr_letters:
#   password.push(random.choice(letters))
#   for symbol in nr_symbols:
#     password.push(random.choice(symbols))
#     for numbers in nr_numbers:
#       password.push(random.choice(numbers))
#
# print(password.join)
#
# Didn't work...
#
# Second Attempt
# password = ""
#
# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)
#   for sym in range(1, nr_symbols + 1):
#       password += random.choice(symbols)
#       for num in range(1, nr_numbers + 1):
#         password += random.choice(numbers)
#
# cryptic_password = random.shuffle(password)
#
# print("Password before scrambling:", password)
# print("Password after scrambled egg:", cryptic_password)
#
# Doesn't work with cryptic, when removing and just leaving line 160 it seems to print a pointer?
# Due to indenting???
#
# Watched solution but will re-try tomorrow...
#
# Third Attempt
#
# password = []
#
# for char in range(1, nr_letters + 1):
#     password.append(random.choice(letters))
# for char in range(1, nr_symbols + 1):
#     password.append(random.choice(symbols))
# for char in range(1, nr_numbers + 1):
#     password.append(random.choice(numbers))
#
# print(password)
# random.shuffle(password)
# print(password)
# cryptic = ''.join(password)
# print(cryptic)
#
# can't leave the parentheses blank for methods, i.e. password.join()
#
# can also same as join, by creating an empty string, using for loop to add chars to it