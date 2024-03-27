#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

######################## MY SOLUTION ########################

import random
from art import logo

print(logo)
no_more_guesses = False
guesses = 0
my_number = 0

difficulty = input("Hard or Easy mode? ").lower()

if difficulty == "easy":
    guesses = guesses + 10
else:
    guesses = guesses + 5

print(f"You have {guesses} guesses...")
my_number = random.randint(0, 100)
print(f"pssst... the number is {my_number}")

while no_more_guesses is not True:

    guess = int(input("What sexy number am I thinking of? "))

    if guess == my_number:
        print("You Win!")
        no_more_guesses = True
    elif guess < my_number:
        print("Too low!")
        guesses -= 1
    elif guess > my_number:
        print("Too high!")
        guesses -= 1
    print(f"You have {guesses} guesses left!")

    if guesses == 0:
        print("Game over...")
        no_more_guesses = True

######################## ANGELA SOLUTION ########################

from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0


#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns reamining"""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


#Make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    #Choosing a random number between 1 and 100
    print("Welcome to the guessing game")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    #Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        #Let the user guess a number.
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again...")


#Track the number of turns and reduce by 1 if they get it wrong.

game()
