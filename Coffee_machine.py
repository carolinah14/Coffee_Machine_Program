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


def formatted_report(raw_resources, dollars):
    """Triggers with report prompt, takes the resources dictionary and money variable and returns formated resources"""
    water = raw_resources["water"]
    milk = raw_resources["milk"]
    coffee = raw_resources["coffee"]
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${dollars}"


def resources_comparison(user_input, raw_resources, menu_dict):
    """This function takes the user input and taps into the menu of that item,
     compares each ingredient with the current resources and acts accordingly"""
    for ingredient in menu_dict[user_input]["ingredients"]:
        if int(menu_dict[user_input]["ingredients"][ingredient]) > int(raw_resources[ingredient]):
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def coins():
    """This function asks the user for input and outputs the total amount of coins with 2 decimals"""
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total_amount = float(quarters + dimes + nickels + pennies)
    return f"{total_amount:.2f}"

def after_purchase_resources(user_input, raw_resources, menu_dict):
    """This function takes the user input and dictionaries, and modifies the resources values after the purchase"""
    for ingredient in menu_dict[user_input]["ingredients"]:
        raw_resources[ingredient] -= menu_dict[user_input]["ingredients"][ingredient]
    return raw_resources


on = True
machine_money = 0
menu_options = ["espresso", "latte", "cappuccino"]

while on:
    user_preference = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_preference == "off":
        on = False
    elif user_preference == "report":
        print(formatted_report(resources, machine_money))
    elif user_preference in menu_options:
        if resources_comparison(user_preference, resources, MENU):
            user_money = float(coins())
            if user_money < MENU[user_preference]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                machine_money += MENU[user_preference]["cost"]
                change_money = user_money - MENU[user_preference]["cost"]
                if change_money != 0:
                    print(f"Here is ${change_money:.2f} dollars in change.")
                resources = after_purchase_resources(user_preference, resources, MENU)
                print(f"Here is your {user_preference}☕. Enjoy!")
        else:
            continue

