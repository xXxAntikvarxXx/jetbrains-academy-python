# Write your code here
from enum import Enum


class CoffeeMachineStates(Enum):
    WAIT_ACTION = 0x000001
    EXECUTE_ACTION = 0x000002
    WAIT_COFFEE_TYPE = 0x000003
    WAIT_FILL_WATER = 0x000004
    WAIT_FILL_MILK = 0x000005
    WAIT_FILL_COFFEE_BEANS = 0x000006
    WAIT_FILL_CUPS = 0x000007
    DONE = 0x000008


class CoffeeMachineAction(Enum):
    NO_ACTION = "no_action"
    BUY = "buy"
    FILL = "fill"
    REMAINING = "remaining"
    TAKE = "take"
    EXIT = "exit"

    @classmethod
    def get_action(cls, name):
        return getattr(cls, name.upper(), None)


class CoffeeMachine:
    ACTIONS_WITH_INPUT = [
        CoffeeMachineAction.BUY,
        CoffeeMachineAction.FILL
    ]
    COFFEE_INGREDIENTS = {
        # Espresso
        1: {
            "water": 250,
            "coffee_beans": 16,
            "cups": 1,
            "money": 4
        },
        # Latte
        2: {
            "water": 350,
            "milk": 75,
            "coffee_beans": 20,
            "cups": 1,
            "money": 7
        },
        # Cappuccino
        3: {
            "water": 200,
            "milk": 100,
            "coffee_beans": 12,
            "cups": 1,
            "money": 6
        }
    }

    def __init__(
            self,
            water=400,
            milk=540,
            coffee_beans=120,
            money=550,
            cups=9
    ):
        self._state = CoffeeMachineStates.WAIT_ACTION
        self._action = CoffeeMachineAction.NO_ACTION
        self._resources = {
            "water": water,
            "milk": milk,
            "coffee_beans": coffee_beans,
            "money": money,
            "cups": cups
        }

    @property
    def state(self):
        return self._state

    def _reset_action(self):
        self._state = CoffeeMachineStates.WAIT_ACTION
        self._action = CoffeeMachineAction.NO_ACTION

    def action(self, input_data):
        if self._state == CoffeeMachineStates.WAIT_ACTION:
            self._action = CoffeeMachineAction.get_action(input_data)
            self._state = CoffeeMachineStates.EXECUTE_ACTION
        if self._action != CoffeeMachineAction.NO_ACTION:
            method = getattr(self, self._action.value, None)
            if method is not None and callable(method):
                if self._action in self.ACTIONS_WITH_INPUT:
                    return method(input_data)
                return method()

    def exit(self):
        self._reset_action()
        self._state = CoffeeMachineStates.DONE

    def remaining(self):
        print()
        print("The coffee machine has:")
        print(self._resources.get("water", 0), "of water")
        print(self._resources.get("milk", 0), "of milk")
        print(self._resources.get("coffee_beans", 0), "of coffee beans")
        print(self._resources.get("cups", 0), "of disposable cups")
        print("$" + str(self._resources.get("money", 0)), "of money")
        self._reset_action()

    def take(self):
        print("I gave you $" + str(self._resources.get("money", 0)))
        self._resources["money"] = 0
        self._reset_action()

    def fill(self, input_data):
        if self._state == CoffeeMachineStates.EXECUTE_ACTION:
            self._state = CoffeeMachineStates.WAIT_FILL_WATER
            return "Write how many ml of water do you want to add:"
        elif self._state == CoffeeMachineStates.WAIT_FILL_WATER:
            self._resources["water"] += int(input_data)
            self._state = CoffeeMachineStates.WAIT_FILL_MILK
            return "Write how many ml of milk do you want to add:"
        elif self._state == CoffeeMachineStates.WAIT_FILL_MILK:
            self._resources["milk"] += int(input_data)
            self._state = CoffeeMachineStates.WAIT_FILL_COFFEE_BEANS
            return "Write how many grams of coffee beans do you want to add:"
        elif self._state == CoffeeMachineStates.WAIT_FILL_COFFEE_BEANS:
            self._resources["coffee_beans"] += int(input_data)
            self._state = CoffeeMachineStates.WAIT_FILL_CUPS
            return ("Write how many disposable cups of coffee do you want "
                    "to add:")
        elif self._state == CoffeeMachineStates.WAIT_FILL_CUPS:
            self._resources["cups"] += int(input_data)
            self._reset_action()

    def _no_ingredients(self, ingredients):
        return [
            ingredient
            for ingredient, value in ingredients.items()
            if self._resources.get(ingredient) < value
        ]

    def _make_coffee(self, coffee_type):
        ingredients = self.COFFEE_INGREDIENTS.get(coffee_type)
        if ingredients is not None:
            no_ingredients = self._no_ingredients(ingredients)
            if not no_ingredients:
                self._resources["water"] -= ingredients.get("water", 0)
                self._resources["milk"] -= ingredients.get("milk", 0)
                self._resources["coffee_beans"] -= ingredients.get(
                    "coffee_beans", 0
                )
                self._resources["cups"] -= ingredients.get("cups", 0)
                self._resources["money"] += ingredients.get("money", 0)
                print("I have enough resources, making you a coffee!")
            else:
                print("Sorry, not enough " + ", ".join(no_ingredients) + "!")
        self._reset_action()

    def buy(self, input_data):
        if self._state == CoffeeMachineStates.EXECUTE_ACTION:
            self._state = CoffeeMachineStates.WAIT_COFFEE_TYPE
            return ("What do you want to buy? 1 - espresso, 2 - latte, "
                    "3 - cappuccino, back - to main menu")
        elif self._state == CoffeeMachineStates.WAIT_COFFEE_TYPE:
            if input_data == "back":
                self._reset_action()
            else:
                self._make_coffee(int(input_data))


def get_input_data(message, empty_string=False):
    empty_string and print()
    print(message)
    return input()


message = "Write action (buy, fill, take, remaining, exit):"
empty_string = True
coffee_machine = CoffeeMachine()
while coffee_machine.state != CoffeeMachineStates.DONE:
    input_data = get_input_data(message, empty_string)
    message = coffee_machine.action(input_data)
    empty_string = False
    if message is None:
        message = "Write action (buy, fill, take, remaining, exit):"
        empty_string = True
