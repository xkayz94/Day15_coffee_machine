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

profit = 0


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resources_sufficient(resource_data,ordered_drink):
    """Check if its enough resources"""
    for item in ordered_drink:
        if ordered_drink[item] > resource_data[item]:
            print(f'Sorry there is not enough {item}')
            return False
        else:
            print('Enough resources')
            return True

def coins():
    """Payment"""
    total = float(input('How many quarters:')) * 0.25
    total += float(input('How many dimes:')) * 0.10
    total += float(input('How many nickles:')) * 0.05
    total += float(input('How many pennies:')) * 0.01
    return total

def transaction(user_amount, price):
    """Check transcaction"""
    if user_amount >= price:
        global profit
        change = round(user_amount - price, 2)
        print(f'Your change is {change} $')
        profit += price
        return True
    else:
        print('“Sorry thats not enough money. Money refunded.')
        return False

def coffe(drink_choice, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Thats your {drink_choice}')

should_work = True

while should_work:
    choice = input('What would you like?: (espresso/latte/cappuccino):')
    if choice == 'off':
        print('Goodbye')
        should_work = False
    elif choice == 'report':
        print(f'Water: {resources['water']}ml')
        print(f'Milk: {resources['milk']}ml')
        print(f'Coffee: {resources['coffee']}g')
        print(f'Money: {profit}$')
    else:
        drink = MENU[choice]
        if resources_sufficient(resources, drink['ingredients']):
            payment = coins()
            if transaction(payment, drink['cost']):
                coffe(choice, drink['ingredients'])

