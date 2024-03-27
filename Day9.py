# TASK ONE - Python Dictionaries

# programming_dictionary = {
#   "Bug": "An error in a program that prevents the program from running as expected.", 
#   "Function": "A piece of code that you can easily call over and over again.",
# }

# #Retrieving items from dictionary.
# print(programming_dictionary["Function"])

# #Adding new items to dictionary.
# programming_dictionary["Loop"] = "The action of doing something over and over again."

# #Create an empty dictionary.
# empty_dictionary = {}

# #Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# #Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer."
# programming_dictionary["Function"] = "A piece of code that you can easily call over and over again."
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# # print(programming_dictionary)

# #Loop through a dictionary
# for key in programming_dictionary:
#   print(f"{key}:")
#   print(programming_dictionary[key])

# #######################################

# #Nesting 
# capitals = {
#   "France": "Paris",
#   "Germany": "Berlin",
# }

# #Nesting a List in a Dictionary

# travel_log = {
#   "France": ["Paris", "Lille", "Dijon"],
#   "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

# #Nesting Dictionary in a Dictionary

# travel_log = {
#   "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#   "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
# }

# #Nesting Dictionaries in Lists

# travel_log = [
# {
#   "country": "France", 
#   "cities_visited": ["Paris", "Lille", "Dijon"], 
#   "total_visits": 12,
# },
# {
#   "country": "Germany",
#   "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#   "total_visits": 5,
# },
# ]


# TASK TWO - Dict Score Grades

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# student_grades = {}

# for student in student_scores:
#   score = student_scores[student]
#   if (score > 90):
#     student_grades[student] = "Outstanding"
#   elif score >80:
#     student_grades[student] = "Exceeds Expectations"
#   elif score >70:
#     student_grades[student] = "Acceptable"
#   else:
#     student_grades[student] = "Fail"
  
# print(student_grades)


# TASK THREE - Nesting Dicts

# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 10},
#     "Italy": {"cities_visited": ["Milan", "Rome", "Sicily"], "total_visits": 3}
# }

# for country, info in travel_log.items():
#     print(f"Country: {country}")
#     print(f"Total visits: {info['total_visits']}")
#     print("Cities visited:")
#     for city in info['cities_visited']:
#         print(f"- {city}")
#     print()

# print("\n###############\n")

# for key, value in travel_log.items():
#     print(f"Country: {key}")
#     print(f"Visits: {value['total_visits']}")
#     print(f"Cities Visited:")
#     for cities in value['cities_visited']:
#         print(f"- {cities}")
#     print()

# Changed to a list of dicts

# travel_log = [
#     {
#         "country": "France", 
#         "cities_visited": ["Paris", "Lille", "Dijon"], 
#         "total_visits": 12
#     },
#     {
#         "country": "Germany", 
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
#         "total_visits": 10
#     },
#     {
#         "country": "Italy", 
#         "cities_visited": ["Milan", "Rome", "Sicily"], 
#         "total_visits": 3
#     }
# ]

# for info in travel_log:
#     print(f"Country: {info['country']}")
#     print(f"Total visits: {info['total_visits']}")
#     print("Cities visited:")
#     for city in info['cities_visited']:
#         print(f"- {city}")
#     print()


# TASK FOUR - Add new countries to a dict

# country = input() # Add country name
# visits = int(input()) # Number of visits
# list_of_cities = eval(input()) # create list from formatted string, MUST be in string list format

# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]


# def add_new_country(name, times_visited, cities_visited):
#   new_country = {}
#   new_country["country"] = name
#   new_country["visits"] = times_visited
#   new_country["cities"] = cities_visited
#   travel_log.append(new_country)


# add_new_country(country, visits, list_of_cities)
# print(travel_log)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")



# TASK FIVE - Bidding Wars!!!

# First attempt
# logo = "Art"
# print(logo)

# bidders = {}
# another_bid = True

# while another_bid == True:

#     bidder_name = input("What is your bidders name? ")
#     bidder_price = int(input("What is their bid? £"))
#     bidders[bidder_name] = bidder_price
#     print(bidders)

#     new_bidder = input("Are there any other bidders? ").lower()

#     if new_bidder == 'no':
#         another_bid == False
#         print("Thanks for the bids, here's the top bid...")


# Code along attempt

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
print()

bidders = {}
another_bid = True

# Function to find highest bid

def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_admount = bidding_record[bidder]
        if bid_admount > highest_bid:
            highest_bid = bid_admount
            winner = bidder
    print(f"\n\nThe winner is {winner} with a bid of £{highest_bid}")
    print()
    print(f"\nHere were the individual bidders -\n")

    for bid in bidding_record:
        print(f"\tBidder: {bid}")
        print(f"\tBid amount: £{bidding_record[bid]}\n")

# While loop to add bids, if wanted

while another_bid == True:

    bidder_name = input("\nWhat is your bidders name?: ")
    bidder_price = int(input("What is their bid?: £"))
    bidders[bidder_name] = bidder_price

    new_bidder = input("Are there any other bidders? 'yes' or 'no': ").lower()

    if new_bidder == 'no':
        another_bid = False
        find_highest_bid(bidders)
