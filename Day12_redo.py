import random

logo = """+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+
 |G|u|e|s|s| |t|h|e| |n|u|m|b|e|r|
 +-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+"""
EASY_LEVEL_TURNS = 7
HARD_LEVEL_TURNS = 5

game_over = False

#Check guess against answer
def check_answer(guess, answer, turns):
    """Checks answer against guess, returns number of turns remaining"""
    if guess > answer:
        print("\nWRONG\nToo High...!")
        return turns - 1
    elif guess < answer:
        print("\nWRONG\nToo Low!")
        return turns - 1
    else:
        print(f"Winner! The answer was {answer}")
        

# Choose difficulty
def difficulty():
    select = input("\nSelect the difficulty level... \n\n'Easy' or 'Hard': ").lower()
    if select == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("\n",logo)
    # Choose a number between 1 and 100 
    print("\nWelcome to the Number Guessing Game!")
    print("\nI'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)

    # User picks difficulty
    turns = difficulty()


    guess = 0
    while guess != answer:
        # User guesses number
        print(f"\n\t{turns} attempts remaining")
        guess = int(input("\n\tGuess a number: "))
        turns = check_answer(guess, answer, turns)
        if turns <= 0:
            print("\nGame over, you lose")
            print(f"\n\tThe answer was {answer}\n")
            return
        elif guess != answer:
            print("\n\t\tGuess again...\n")

game()

# FIRST ATTEMPT
# lives = 0
# game_over = False

# while game_over != True:
#     def play_game():
#         print(logo)

#         def difficulty():
#             select = input("What difficulty? 'Easy', 'Medium' or 'Hard'").lower()
#             if select == 'Easy':
#                 lives = 10
#             elif select == 'Medium':
#                 lives = 5
#             else:
#                 lives = 3
#             return lives
#         difficulty()

#         def guess_number():
#             number = random.randint(0, 100)
#             guess = int(input("Guess the number"))

#             if guess == number:
#                 print("You win!")
#                 print(f"You had {lives} lives left.")
#             else:
#                 print("Nope!")
#                 lives = lives - 1
#                 print("Your lives are {lives}")

#             if lives <= 0:
#                 print("Outta lives, you lose")
#                 game_over = True
        
#         guess_number()

#     play_game()




