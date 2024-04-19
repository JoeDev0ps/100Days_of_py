# # Dict/Dictionary
# programming_dictionary = {
#     "Bug": "An error in a program.",
#     "Function": "A piece of code that you can call repeatedly",
#     "Loop": "The action of doing something repeatedly",
# }

# programming_dictionary["Conditional"] = "Code that does something depending if true, or false"


# # i variable gives keys, dict[i] gives value
# for i in programming_dictionary:
#     print(i + ": " + programming_dictionary[i])


# my_list = []


# # Nesting
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# # Nesting a list in a dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }

# list_nested = ["A", "B", ["C", "D"]]

# Nesting a dict in a dict

# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"]},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"]},
#     "Italy": {"cities_visited": ["Rome", "Milan", "Pisa"]},
#     "The Moon": {"Space": ["Deep", "Vacuum", "Cold"]},
#     "The Sun": ["Hot", "Fire", "Solar"],
#     "Spain": {"cities_visited": []},
# }


# for key in travel_log:
#     print()
#     print(f"Key: {key}")
#     print(f"Value: {travel_log[key]}")
#     # Checks if value is nested dict
#     if isinstance(travel_log[key], dict):
#         # Checks if cities_visited is name of dict key
#         if 'cities_visited' in travel_log[key]:
#             cities = travel_log[key]['cities_visited']
#             # Checks if cities_visited key contains anything
#             if not cities:
#                 print("No cities here")
#             else:
#                 # iterates over the cities list and prints just the city name
#                 for city in cities:
#                     print(f"City: {city}")
#         else:
#             print("No cities here")
#     else:
#         print("No cities here")

# Would not work on line 53, as would check if the value of the key 'France' for example is the string 'cities_visited'
# However, the value is actually a key to another dict that is nested...
# if travel_log[key] == "cities_visited"


# List with nested dictionaries

# travel_log = [
#     {
#     "Country": "France", 
#     "cities_visited": ["Paris", "Lille", "Dijon"],
#     "Visits": 4
#     },
#     {
#     "Country": "Germany", 
#     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#     "Visits": 6
#     },
#     {
#     "Country": "Italy", 
#     "cities_visited": ["Rome", "Milan", "Pisa"],
#     "Visits": 2
#     },
# ]


# Bid program - my attempt
# bid_amount = 0
# bidders = {}
# stillBidding = True


# def highest_bid(bidders):
#     highest_bidder = None
#     for bidder in bidders:
#         highest_bidder = bidders[bidder]
#         if bidder > highest_bidder:
#             highest_bidder = bid
#     print()
#     print(f"The winning bidder was {bidder}\nThe highest bid was: £{highest_bidder}")

      

# while stillBidding is True:

#   name = input("what's your name? ")
#   bid = int(input("What's your bid? £ "))

#   bidders[name] = bid  # Store name and bid amount in dictionary

#   print("Current bidders:")
#   for bidder, bid in bidders.items():
#     print(f"Bidder: {bidder}")  # Print bidder name and bid

#   more_bidding = input(
#       "Any more bids? 'Y' for 'Yes', 'N' for 'No'... ").lower()

#   if more_bidding == 'n':
#     for bidder, bid in bidders.items():
#       print(f"Bidder: {bidder} \nBid Amount: £{bid}")
#       highest_bid(bidder)
#     break
#   else:
#     clear()
#     print(logo)
#     continue


# Re-attempt at bid program - need to refine my highest_bidder function
# from replit import clear  
# from art import logo
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bids = {}
bidding_finished = False


# FUNCTION ONE - FAULTY
# Incorrect update in function 1: Inside the loop in function 1, 
# it assigns the current bidder's value (bids[bidder]) to highest_bid unconditionally. 
# This overwrites the previous highest bid value on every iteration, 
# even if it's not actually higher.

# def highest_bidder(bids):
#   highest_bid = 0
#   winner = ""
#   for bidder in bids:
#     highest_bid = bids[bidder]
#     if bids[bidder] > highest_bid:
#       highest_bid = bids[bidder]
#       winner = bidder
#   print(f"The winner is {winner}")
#   print(f"Their bid was £{highest_bid}")


# FUNCTION TWO - WORKING
def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
     if bidding_record[bidder] > highest_bid:
        highest_bid = bidding_record[bidder]
        winner = bidder
  print(f"The winner is {winner}")
  print(f"Their bid was £{highest_bid}")


while not bidding_finished:  
	name = input("What's your name? ")
	try:
		price = int(input("What's your bid? £"))
	except ValueError:
		print("Not a valid number")
	bids[name] = price
	keep_playing = input("Do you want to add bidders? Y or N ").lower()
	if keep_playing == "n":
		highest_bidder(bids)
		bidding_finished = True
	else:
	#	clear()
		print(logo)
		continue
  