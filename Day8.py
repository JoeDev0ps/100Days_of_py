# TASK ONE - Arguments

# Function
# def greet(name):
#     print(f"Hello... {name}")
#     print(f"How do you do.... {name}")
#     print("Isn't the weather nice today? ")

# greet("Joe")

# Default arguments
# def greet_with_default(name="Joe"):
#     print(f"Hello... {name}")
#     print(f"How do you do.... {name}")
#     print("Isn't the weather nice today? ")

# greet_with_default("Jeremy")
# greet_with_default()
# greet_with_default(None)

# Positional arguments
# def greet_with_pos(name, location):
#     print("Hello " + name)
#     print("What's it like at " + location + " today?")

# greet_with_pos('Joe', 'Cas Vegas')

# Keyword arguments
# def greet_with_key(name, location):
#     print("Hello " + name)
#     print("What's it like at " + location + " today?")

# greet_with_key(location='Classy Cas', name='Joe-a')


# TASK TWO - Rounding up 

# import math

# def paint_calc(height, width, cover):
#     num_cans = (height * width) / cover
#     round_up = math.ceil(num_cans)
#     print(f"You'll need {round_up} cans of paint")


# TASK THREE - Prime number checker

# def prime_checker(number):
#   is_prime = True
#   # checks if any other number than 2 upto the number can divide cleanly to zero
#   for i in range(2, number):
#     if number % i == 0:
#       is_prime = False
#   if is_prime == True:
#     print("It's a prime number.")
#   else:
#     print("It's not a prime number.")

# n = int(input("Check a number... "))
# prime_checker(number=n)


# TASK FOUR - Caeser Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Not added art to folder structure...
# from art import logo
# print(logo)

print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts. DONE

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).
  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  
  result = input("Type 'yes' if you want to go again. Otherwise type 'no.'\n").lower()

  if result == 'no':
    should_continue = False
    print("Goodbye")