from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

has_choice = True
menu = Menu()
while (has_choice):
    print(menu.get_items())
    choice = input("Enter with your choice: ")
    #print(menu.find_drink(choice).name)
    cf = CoffeeMaker()
    coins = MoneyMachine()
    if choice.lower() == "off":
        has_choice = False
        #exit()
    elif choice.lower() == "report":
        cf.report()
    elif menu.find_drink(choice).name == "espresso":
        if cf.is_resource_sufficient(menu.find_drink(choice)):
            if coins.make_payment(menu.find_drink(choice).cost):
                cf.make_coffee(menu.find_drink(choice))
    elif menu.find_drink(choice).name == "latte":
        if cf.is_resource_sufficient(menu.find_drink(choice)):
            if coins.make_payment(menu.find_drink(choice).cost):
                cf.make_coffee(menu.find_drink(choice))
    elif menu.find_drink(choice).name == "cappuccino":
        if cf.is_resource_sufficient(menu.find_drink(choice)):
            if coins.make_payment(menu.find_drink(choice).cost):
                cf.make_coffee(menu.find_drink(choice))

    # elif choice.lower() == "latte":
    #     if check_resources(choice.lower()):
    #         coins(choice.lower())
    #     else:
    #         print("No resources")
    # elif choice.lower() == "cappuccino":
    #     if check_resources(choice.lower()):
    #         coins(choice.lower())
    #     else:
    #         print("No resources")