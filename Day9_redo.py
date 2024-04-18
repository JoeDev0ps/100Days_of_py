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


# Bid program
bid_amount = 0
bidders = {}
stillBidding = True


def highest_bid():
    highest_bidder = None
    for bidder, bid in bidders.items():
        if bid > bid_amount:
            bid_amount = bid
            highest_bidder = bidder

    return highest_bidder

      

while stillBidding is True:

  name = input("what's your name? ")
  bid = int(input("What's your bid? £ "))

  bidders[name] = bid  # Store name and bid amount in dictionary

  print("Current bidders:")
  for bidder, bid in bidders.items():
    print(f"Bidder: {bidder}")  # Print bidder name and bid

  more_bidding = input(
      "Any more bids? 'Y' for 'Yes', 'N' for 'No'... ").lower()

  if more_bidding == 'n':
    for bidder, bid in bidders.items():
      print(f"Bidder: {bidder} \nBid Amount: £{bid}")
      print()
      print(f"The winning bid was {highest_bid}")
    break
  else:
    continue
