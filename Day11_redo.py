############### Blackjack Project #####################
import random
import math
# import clear
# from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# print(logo)
another_game = False

player_hand = []
dealer_hand = []
dealer_score = sum(dealer_hand, len(dealer_hand))
player_score = sum(player_hand, len(player_hand))


player_hand.append(random.choice(cards))
dealer_hand.append(random.choice(cards))

def deal_card():
    player_hand.append(random.choice(cards))
    print("Player Hand")
    print(player_hand)
    twist = input("What you like another card? 'Y' or 'N'").lower()
    
    if twist == 'y':
        deal_card()
    else:
        dealer_turn()

def dealer_turn():
    dealer_hand.append(random.choice(cards))
    print("Dealer Hand")
    print(dealer_hand)

    if dealer_score == 21:
        print("Dealer has blackjack, you lose")
        print(dealer_hand)  
    elif dealer_score > 21:
        print("Dealer Bust")
    elif dealer_score == 17:
        print(f"Dealer Hand: {dealer_hand}")
    else:
        dealer_turn()

def compare_hands():
    if player_score > dealer_score and player_score <= 21:
        print("Player wins")
    else:
        print("Dealer wins")

deal_card()
compare_hands()


# ACCIDENTAL INFINITE LOOP

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

