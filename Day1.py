# Original print statement
#
#print("Hello " + input("What is your name?") + "!")

#------------------------------------------------

# Len can be imbedded into input, which can be all embedded into print!
#
# print(len("Hello " + input("What is your name?") + "!"))

#------------------------------------------------

# A = 41, B = 29, Swaps'em!
# a = input()
# b = input()

# # We need a third variable to swap, imagine 3 cups and 2 are full...
# thirdVar = a
# a = b
# b = thirdVar 

# print("a: " + a)
# print("b: " + b)

#------------------------------------------------

# My attempt at a band name generator
#
print("WELCOME TO HELL...")
def bandGenerator():
    city_name = input("What's your home city?\n")
    pet_name = input("What's your pet name?\n")
    print(city_name + " " + pet_name)

bandGenerator() 