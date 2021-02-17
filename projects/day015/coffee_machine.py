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
    "money": 0
}


def has_resources(selected_drink):
    for key in resources:
        if key in selected_drink["ingredients"]:
            if resources[key] < selected_drink["ingredients"][key]:
                print(f"Sorry, there is not enough {key}.\n")
                return False
    return True


def make_coffee(selected_drink, selected_drink_name):
    for key in resources:
        if key in selected_drink["ingredients"]:
            resources[key] -= selected_drink["ingredients"][key]
    print(f"Here is your {selected_drink_name} ☕ Enjoy!\n")


def transaction_successful(amount, selected_drink):
    if amount >= selected_drink["cost"]:
        resources["money"] += selected_drink["cost"]
        change = amount - selected_drink["cost"]
        if change > 0:
            print(f"Here is ${'{:.2f}'.format(change)} in change.")
        return True
    else:
        print("Sorry, that is not enough money. Money refunded.\n")
        return False


def print_menu():
    str_menu = "("
    for key in MENU:
        str_menu += f"{key}=${'{:.2f}'.format(MENU[key]['cost'])}/"
    str_menu = str_menu[:-1] + ")"
    return str_menu


def print_report():
    for key in resources:
        if key == "coffee":
            print(f"{key.title()}: {resources[key]}g")
        elif key == "money":
            print(f"{key.title()}: ${'{:.2f}'.format(resources[key])}")
        else:
            print(f"{key.title()}: {resources[key]}ml")
    print("\n")


is_machine_on = True

while is_machine_on:
    command = input(f"What would you like? {print_menu()}: ").lower()

    if command == "espresso" or command == "latte" or command == "cappuccino":
        drink = MENU[command]
        drink_name = command.title()
        if has_resources(drink):
            print("Please insert coins.")
            quarters = float(input("How many quarters? "))
            dimes = float(input("How many dimes? "))
            nickles = float(input("How many nickels? "))
            pennies = float(input("How many pennies? "))
            total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
            if transaction_successful(total, drink):
                make_coffee(drink, drink_name)
    elif command == "report":
        print_report()
    elif command == "off":
        is_machine_on = False
    else:
        print("Type the name of the wanted drink, e.g., espresso.\n")
