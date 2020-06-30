# Write your code here
coffee_resources = {
    "water": 400,
    "milk": 540,
    "coffee_beans": 120,
    "money": 550,
    "cups": 9
}
coffee_ingredients = {
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


def print_coffee_machine():
    print()
    print("The coffee machine has:")
    print(coffee_resources.get("water", 0), "of water")
    print(coffee_resources.get("milk", 0), "of milk")
    print(coffee_resources.get("coffee_beans", 0), "of coffee beans")
    print(coffee_resources.get("cups", 0), "of disposable cups")
    print(coffee_resources.get("money", 0), "of money")


def _no_ingredients(ingredients):
    no_ingredients = []
    for ingredient, value in ingredients.items():
        if coffee_resources.get(ingredient) < value:
            no_ingredients.append(ingredient)
    return no_ingredients


def make_coffee(coffee_type):
    ingredients = coffee_ingredients.get(coffee_type)
    if ingredients is not None:
        no_ingredients = _no_ingredients(ingredients)
        if not no_ingredients:
            coffee_resources["water"] -= ingredients.get("water", 0)
            coffee_resources["milk"] -= ingredients.get("milk", 0)
            coffee_resources["coffee_beans"] -= ingredients.get(
                "coffee_beans", 0
            )
            coffee_resources["cups"] -= ingredients.get("cups", 0)
            coffee_resources["money"] += ingredients.get("money", 0)
            print("I have enough resources, making you a coffee!")
        else:
            print("Sorry, not enough " + ", ".join(no_ingredients) + "!")


def buy():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, "
          "back - to main menu")
    coffee_type = input()
    if coffee_type != "back":
        coffee_type = int(coffee_type)
        make_coffee(coffee_type)


def fill():
    print("Write how many ml of water do you want to add:")
    coffee_resources["water"] += int(input())
    print("Write how many ml of milk do you want to add:")
    coffee_resources["milk"] += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    coffee_resources["coffee_beans"] += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    coffee_resources["cups"] += int(input())


def take():
    print("I gave you $" + str(coffee_resources.get("money", 0)))
    coffee_resources["money"] = 0


def get_action():
    print()
    print("Write action (buy, fill, take, remaining, exit)")
    return input()


actions = {
    "buy": buy,
    "fill": fill,
    "take": take,
    "remaining": print_coffee_machine,
}

action = get_action()
while action != "exit":
    actions.get(action, (lambda: None))()
    action = get_action()
