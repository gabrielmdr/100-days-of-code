from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

obj_coffee_maker = CoffeeMaker()
obj_menu = Menu()
obj_money_machine = MoneyMachine()

is_machine_on = True

while is_machine_on:
    command = input(f"What would you like? {obj_menu.get_items()}: ")
    if command == "report":
        obj_coffee_maker.report()
    elif command == "off":
        is_machine_on = False
    else:
        drink = obj_menu.find_drink(command)
        if drink is not None:
            if obj_coffee_maker.is_resource_sufficient(drink):
                if obj_money_machine.make_payment(drink.cost):
                    obj_coffee_maker.make_coffee(drink)
