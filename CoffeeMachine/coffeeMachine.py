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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

QUARTER = 0.25
DIMES = 0.1
NICKEL = 0.05
PENNIES = 0.01

def check_resources(choice):
    water = resources["water"] - MENU[choice]["ingredients"]["water"]
    coffee = resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
    if choice != "espresso":
        milk = resources["milk"] - MENU[choice]["ingredients"]["milk"]
    if choice == "espresso" and water > 0 and coffee > 0:
        resources["water"] = water
        resources["coffee"] = coffee
        return True
    elif choice == "latte" and water > 0 and coffee > 0 and milk > 0:
        resources["water"] = water
        resources["coffee"] = coffee
        resources["milk"] = milk
        print(resources)
        return True
    elif choice == "cappuccino" and water > 0 and coffee > 0 and milk > 0:
        resources["water"] = water
        resources["coffee"] = coffee
        resources["milk"] = milk
        return True


def enough_funds(choice, total):
    if choice == "espresso":
        if total - MENU[choice]["cost"] >= 0:
            change = total - MENU[choice]["cost"]
            print(f"Here is $ {round(change, 2)} in change")
            print("Here is your espresso ☕️. Enjoy")
        else:
            print("Sorry that is not enough money. Money refunded")
    elif choice == "latte":
        if total - MENU[choice]["cost"] >= 0:
            change = total - MENU[choice]["cost"]
            print(f"Here is $ {round(change, 2)} in change")
            print(f"Here is your {choice} ☕️. Enjoy")
        else:
            print("Sorry that is not enough money. Money refunded")
    else:
        if total - MENU[choice]["cost"] >= 0:
            change = total - MENU[choice]["cost"]
            print(f"Here is $ {round(change, 2)} in change")
            print(f"Here is your {choice} ☕️. Enjoy")
        else:
            print("Sorry that is not enough money. Money refunded")


def coins(choice):
    print("Please insert coins.")
    #quarters = int(input("How many quarters?: "))
    quarters = 10
    #dimes = int(input("How many dimes?: "))
    dimes = 10
    #nickels = int(input("How many nickels?: "))
    nickels = 5
    #pennies = int(input("How many pennies?: "))
    pennies = 5
    total = quarters*QUARTER + dimes*DIMES + nickels*NICKEL + pennies*PENNIES
    enough_funds(choice, total)


has_choice = True
while (has_choice):
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice.lower() == "off":
        has_choice = False
        #exit()
    elif choice.lower() == "report":

        print(f"Water: {resources['water']} ml")
        print(f"Coffee: {resources['coffee']} ml")
        print(f"Milk: {resources['milk']} ml")


    elif choice.lower() == "espresso":
        if check_resources(choice.lower()):
            coins(choice.lower())
        else:
            print("No resources")
    elif choice.lower() == "latte":
        if check_resources(choice.lower()):
            coins(choice.lower())
        else:
            print("No resources")
    elif choice.lower() == "cappuccino":
        if check_resources(choice.lower()):
            coins(choice.lower())
        else:
            print("No resources")


