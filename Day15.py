MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

money = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

menu = ("\nHere's our selection of Beverages:\n\n1. Tea COMING SOON"
        "\n2. Black Coffee (Filtered) COMING SOON\n3. Latte\n4. Cappuccino"
        "\n5. Espresso\n6. Type 'Report' to see levels\n7. Type 'Off' to Exit\n")

print(menu)


def is_resource_sufficient(order_ingredients):
    """Returns True if the beverage can be made, or False is not"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}...")
            return False
    return True


def process_coins():
    """Returns the total amount of money from coins inserted"""
    print("Please insert coins")
    total = int(input("Insert Quarters: ")) * 0.25
    total += int(input("Insert Dimes: ")) * 0.1
    total += int(input("Insert Nickles: ")) * 0.05
    total += int(input("Insert Pennies: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True if payment is accepted, otherwise False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change: ${change}")
        global money
        money += drink_cost
        return True
    else:
        print("Not enough money! Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Makes coffee and deducts the resources used from our total resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")


is_on = True


# Loop to prompt for orders until cannot or specified not to
while is_on:
    choice = input("What type of beverage would you like? ").lower()

# 'Turn off' coffee machine
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])

# CHAT GPT Solution
#     print(f"{item}:")
#     for ingredient, amount in MENU[item]['ingredients'].items():
# for item in MENU:
#         print(f"{ingredient}: {amount}")
# for resource, amount in resources.items():
#     print(f"{resource}: {amount}")
# break

# money = 1 * quarters
# money = 1 * dimes
# money = 1 * nickles
# money = 1 * pennies

# if choice == MENU[choice]:
#     if money > MENU["cost"]:
#         print(f"Here's your {choice}, enjoy!")
#     else:
#         print(f"Not enough money, please come back with me...")
#         break

# elif choice == 'report':
#     for x in MENU:
#         print(["ingredients"]["water"])
#         print(["ingredients"]["milk"])
#         print(["ingredients"]["coffee"])
#         break

# TODO: 1. Store and print report of resources (minus ingredients used)
# TODO: 2. Check sufficient resources to make order
# TODO: 3. Work in Pycharm and double check in VSCode
