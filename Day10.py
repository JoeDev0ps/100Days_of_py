# TASK ONE - Format first & last names

# def format_name(f_name, l_name):
#     full = f_name.title() + " " + l_name.title()
#     print(f"There are {len(full)} characters in:")
#     return f"{full}"

# print(format_name("jOe", "bAloney"))

# Version 2

# def format_name_two(f_name, l_name):
#     full = f_name + " " + l_name
#     print(f"There are {len(full)} characters in:")
#     return f"{full.title()}"

# print(format_name("jOe", "bAloney"))

# Version 3

# def format_name(f_name, l_name):
#   """Take a first and last name and format it 
#   to return the title case version of the name."""
#   if f_name == "" or l_name == "":
#     return "You didn't provide valid inputs."
#   formated_f_name = f_name.title()
#   formated_l_name = l_name.title()
#   return f"Result: {formated_f_name} {formated_l_name}"

# print(format_name(input("What is your first name? "), input("What is your last name? ")))


# TASK TWO - Leap year months

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False
  
# def days_in_month(year, month):
#   """Calculates if a leap year, if True returns 29 days for February"""
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
#   if is_leap(year) == True:
#     month_days[1] = 29
#     return month_days[1]
#   else:
#     # month - 1 is taking account for zero-based indexing when inputting 2 for february, for example
#     return month_days[month - 1]
  
# year = int(input()) # Enter a year
# month = int(input()) # Enter a month
# days = days_in_month(year, month)
# print(days)


# TASK THREE - Calculator 

# print("\nHere's a calculator, below are the operators!\n")
# print("Add +\nSubtract -\nMutiply *\nDivide /\nSquare s\n")

# number_one = int(input("Select your first number... "))
# number_two = int(input("Select your second number... "))
# operator = input("Select your operator... '+', '-', '*', '/' or '**' ")

# print()

# if operator == '+':
#     print(f"The answer is {number_one + number_two}")
# elif operator == '-':
#     print(f"The answer is {number_one - number_two}")
# elif operator == '*':
#     print(f"The answer is {number_one * number_two}")
# elif operator == '/':
#     print(f"The answer is {number_one / number_two}")
# else:
#     print(f"The answer is {number_one ** number_two}")

# Version 2
    
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def exponent(n1, n2):
    return n1 ** n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": exponent
}

calculate_sum = True

# Embedding all logic in a while loop

while calculate_sum == True:

  number_one = int(input("Select your first number... "))
  number_two = int(input("Select your second number... "))

  for symbol in operations:
      print(symbol)

  operator = input("Which operator are you choosing?: '+', '-', '*', '/' or '^' ")

  # Angela solution
  calculation_function = operations[operator]
  the_answer = calculation_function(number_one, number_two)

  # CHAT GPT solution
  if operator in operations:
      first_answer = operations[operator](number_one, number_two)
      print(f"{number_one} {operator} {number_two} = {first_answer}")
  else:
      print("Invalid operator selected.")

  # Angela solution print check
  print(f"Once again the answer is {the_answer}")

  # A third operation - Angela Version

  operator = input("Pick ANOTHER operator: '+', '-', '*', '/' or '^' ")
  number_three = int(input("Pick a third number: "))
  calculation_function = operations[operator]
  # Below line overrides the first calculation operator
  # second_answer = calculation_function(calculation_function(number_one, number_two), number_three)
  # (3 + 5) * 3 changes to (3 * 5) * 3 = 45

  # Correct line - thanks to pointers
  second_answer = calculation_function(first_answer, number_three)

  print(f"{first_answer} {operator} {number_three} = {second_answer}")

# Condition to break loop or continue

  play_on = input("Shall we do another sum? 'Yes' to continue").lower()

  if play_on == 'yes':
      continue
  else:
      break

# Angela Version - loop always uses answer from the previous sum
  
# ISSUE - no exit loop, always recursively calls or continues while loop
  
from replit import clear

from art import logo


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("+"))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()
