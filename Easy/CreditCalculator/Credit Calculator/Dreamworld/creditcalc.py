# write your code here
from math import ceil


def get_input(message, type_cast=None):
    print(message)
    return type_cast(input()) if type_cast is not None else input()


def monthly_count(principal):
    _payment = get_input("Enter monthly payment:", int)
    _months = ceil(principal / _payment)
    if _months == 1:
        message = f"It takes {_months} month to repay the credit"
    else:
        message = f"It takes {_months} months to repay the credit"
    print(message)


def monthly_payment(principal):
    _months = get_input("Enter count of months:", int)
    _payment = ceil(principal / _months)
    _last_payment = -1
    while _last_payment < 0:
        _last_payment = principal - (_months - 1) * _payment
        if _last_payment < 0:
            _payment -= 1
    message = f"Your monthly payment = {_payment}"
    if _last_payment != _payment:
        message = f"{message} with last month payment = {_last_payment}."
    print(message)


actions = {
    "m": monthly_count,
    "p": monthly_payment
}

credit_principal = get_input("Enter the credit principal:", int)
action = get_input(
    "What do you want to calculate?\n"
    "type \"m\" - for count of months,\n"
    "type \"p\" - for monthly payment:"
)
actions.get(action, (lambda principal: None))(credit_principal)


