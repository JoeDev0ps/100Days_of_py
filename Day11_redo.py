# ############### Blackjack Project #####################
# import random
# import math
# # import clear
# # from art import logo

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# # print(logo)
# another_game = False

# player_hand = []
# dealer_hand = []

# player_hand.append(random.choice(cards))
# dealer_hand.append(random.choice(cards))

# def deal_card():
#     player_hand.append(random.choice(cards))
#     player_score = sum(player_hand)
#     print("Player Hand")
#     print(f"Hand:{player_hand}, Score:{player_score}")
#     twist = input("What you like another card? 'Y' or 'N'").lower()
    
#     if twist == 'y':
#         deal_card()
#     else:
#         return player_score

# def dealer_turn():
#     dealer_hand.append(random.choice(cards))
#     dealer_score = sum(dealer_hand)
#     print("Dealer Hand")
#     print(f"Hand:{dealer_hand}, Score:{dealer_score}")

#     if dealer_score == 21:
#         print("Dealer has blackjack, you lose")
#         print(dealer_hand)  
#     elif dealer_score > 21:
#         print("Dealer Bust")
#     elif dealer_score == 17:
#         print(f"Dealer Hand: {dealer_hand}")
#     else:
#         dealer_turn()

# def compare_hands():
#     if player_score > dealer_score and player_score <= 21:
#         print("Player wins")
#     else:
#         print("Dealer wins")

# deal_card()
# dealer_turn()
# compare_hands()
import random
from time import sleep

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def calculate_score(cards):
    """Takes a list of cards and returns a score for cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0 
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return(sum(cards)) 


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def play_game():

    print(logo)
    
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while is_game_over == False:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour hand: {user_cards}, Current Score: {user_score}")
        sleep(0.6)
        print(f"\nDealer hand: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("\nDo you want another card? 'Y' or 'N' ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
                sleep(0.4)
            else:
                sleep(0.4)
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        sleep(0.6)
        print(f"\nDealer hand: {computer_cards}\nScore: {computer_score}")
        sleep(0.4)


    def compare(user_score, computer_score):
        print()
        if len(user_cards) == 5 and user_score < 21:
            return("Five card charlie 😎")

        if user_score > 21 and computer_score > 21:
            return "You went over. You lose 😤"

        if user_score == computer_score:
            return "Draw 🙃"
        elif computer_score == 0:
            return "Lose, Dealer has Blackjack 😱"
        elif user_score == 0:
            return "Win with a Blackjack 😎"
        elif user_score > 21:
            return "You went over. You lose 😭"
        elif computer_score > 21:
            return "Dealer went over. You win 😁"
        elif user_score > computer_score:
            return "You win 😃"
        else:
            return "You lose 😤"


    print(f"\nYour hand: {user_cards}\nUser Score: {user_score}")
    sleep(0.6)
    print(f"\nDealer hand: {computer_cards}\nDealer Score: {computer_score}")

    print(compare(user_score, computer_score))

while input("\nDo you want to play a game? 'Y' or 'N': ").lower() == "y":
   play_game()

##################### Hints ##################### 