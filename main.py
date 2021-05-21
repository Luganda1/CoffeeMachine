from math import floor

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
price = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "amount": '$ 0'
}


def process_coins():
    """Takes the coins and returns the total amount"""
    amount = int(input("How many quarters?: ")) * 0.25
    amount += int(input("How many dimes?: ")) * 0.1
    amount += int(input("How many nickles?: ")) * 0.05
    amount += int(input("How many pennies?: ")) * 0.01
    return amount


def check_resources(ingridients):
    """Takes user ingredients and returns check if they are sufficient"""
    for item in ingridients:
        if ingridients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_transaction(payment, drinks_cost):
    """Takes payments and calculates if its enough for the drink"""
    if payment >= drinks_cost:
        change = round((payment - drinks_cost), 2)
        print(f"Here is your change ${change}")
        global price
        price += drinks_cost
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(choice, ingridient):
    for item in ingridient:
        resources[item] -= ingridient[item]
        print(f"Here is your {choice}, Enjoy!")


is_machine_on = True

# TODO: 0. Prompt user
while is_machine_on:
    prompt = input("What would you like? (espresso/latte/cappuccino): ")

# TODO: 1. Print a detailed report.
    if prompt == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${price}")
    elif prompt == "off":
        is_machine_on = False
# TODO: 2. Check if resources are sufficient.
    else:
        drink = MENU[prompt]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if process_transaction(payment, drink['cost']):
                make_coffee(prompt, drink["ingredients"])



# TODO: 3. Process coins.



#


# TODO: 4. Check if transactions is successful.
# TODO: 5. Make Coffee
