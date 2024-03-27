#generate art
#randomly generate two users, a & b
#ask for user input which has the highest followers
#if correct loop to second question & increment
#if wrong, total score and exit program

from game_data import data
from art import logo, vs
import random

print(logo)
game_on = True
score = 0

while game_on == True:
  choice_a = random.choice(data)
  choice_b = random.choice(data)
  
  print(choice_a)
  print(vs)
  print(choice_b)
  
  player_guess = input("Who has the most social followers? A or B").lower()
  
  if player_guess == "a" and choice_a[follower_count] > choice_b[follower_count]:
    score += 1
  