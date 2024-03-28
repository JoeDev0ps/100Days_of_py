import random
# from art import logo 
# from replit import clear

logo = "BlackJack Game"
print(logo)
print()


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

player_hand = []
dealer_hand = []

for _ in range(2):
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())


print(player_hand)
print(player_hand)

def calculate_hand(cards):
  """Take a list of cards and return score, also check for blackjack"""
  if sum(cards) == 21 and len(cards) == 2:
    print("BlackJack!")
    return 0
  if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


# def compare_hands(player_score, dealer_score):
#   if player_score == dealer_score:
#     return "Draw"
#   elif dealer_score == 0:
#     return "Player loses, dealer has Blackjack"
#   elif player_score == 0:
#     return "Player wins with Blackjack"
#   elif player_score > 21:
#     return "Bust, player loses"
#   elif dealer_score > 21:
#     return "Dealer bust, Player wins"
#   elif player_score > dealer_score:
#     return "Player wins, player has best hand"
#   else:
#     return "Player loses, dealer has best hand"


# def play_blackjack():

#   game_over = False
    

#   while not game_over:
  
#     player_score = calculate_hand(player_hand)
#     dealer_score = calculate_hand(dealer_hand)
  
#     print(f"Player Hand: {player_hand}, Current Score: {calculate_hand(dealer_hand)}")
#     print(f"Dealer Hand: {dealer_hand[0]}")
  
#     if player_score == 0 or dealer_score == 0 or player_score > 21:
#        game_over = True
#     else:
#       draw = input("Do you want to draw again? Y or N: ").lower
#       if draw == "y":
#         player_hand.append(deal_card())
#       else:
#         game_over = True


#   while dealer_score != 0 and dealer_score < 17:
#      dealer_hand.append(deal_card())
#      dealer_score = calculate_hand(dealer_hand)
  
#   print(f"Player Final Hand: {player_hand}, Final Score: {player_score}")
#   print(f"Dealer Final Hand: {dealer_hand}, Dealer Final Score: {dealer_score}")
#   print(compare_hands(player_score, dealer_score))


# while input("Do you want to play a game of Blackjack? Y or N: ").lower == "y":
#   clear()
#   play_blackjack()