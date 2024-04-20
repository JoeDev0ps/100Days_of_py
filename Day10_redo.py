# # Adding inputs to a function
# def format_name(f_name, l_name):
#     print(f"{f_name} {l_name}".title())

# format_name("joe", "kickass")

# Days in month function - changes Feb to 29 if its a leap year
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
  
# # My solution
# def days_in_month(year, month):
#   # Bad form DocString
#   """Calculates the month
#   and years to calculate
#   if February is a leap year
#   which means 29 days instead
#   of the usual 28 days..."""
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
#   if is_leap(year) == True:
#     month_days[1] = 29
#   return month_days[month - 1]

# # Angela solution
# """Calculates leap year days, adds 1 day to Feb if a leap year"""
# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
#   if month == 2 and is_leap(year):
#     return 29
#   else:
#     return month_days[month - 1]
  
# year = int(input()) # Enter a year
# month = int(input()) # Enter a month
# days = days_in_month(year, month)
# print(days)


# # Calculator project - first ver

# def add(n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return n1 - n2


# def multiply(n1, n2):
#     return n1 * n2


# def divide(n1, n2):
#     return n1 / n2

# operators = {
#     '+': add,
#     '-': subtract,
#     '*': multiply,
#     '/': divide
# }

# num1 = float(input("What's the first number? "))
# num2 = float(input("What's the second number? "))

# for symbol in operators:
#     print(symbol)

# operation_symbol = input("Pick an operator from the list above: Add, Subtract, Multiply or Divide: ")
# first_answer = operators[operation_symbol](num1, num2)

# # add :,.0f to round decimals to a whole int
# print(f"{num1} {operation_symbol} {num2} = {first_answer}")

# num3 = float(input("Pick another number: "))
# operation_symbol = input("Pick another operator: Add, Subtract, Multiply or Divide: ")
# second_answer = operators[operation_symbol](first_answer, num3)
# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

# # If instead of using first_answer we copied the whole line
# # i.e, second_answer = operators[operation_symbol](num1, num2), num3)
# # This would create an error as we'd change the operator of the original function call

# # Calculator project - second ver
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

operators = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    num1 = float(input("What's the first number? "))

    for symbol in operators:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operator from the list above: Add, Subtract, Multiply or Divide: ")
        num2 = float(input("What's the second number? "))
        answer = operators[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        user_dec = input("Type 'y' to continue, 'a' to start again, or 'n' to quit... ").lower()
        
        if user_dec == 'n':
            break
        elif user_dec == 'a':
            should_continue = False
            calculator()
        else:
            num1 = answer
            continue

if __name__ == '__main__':
    calculator()