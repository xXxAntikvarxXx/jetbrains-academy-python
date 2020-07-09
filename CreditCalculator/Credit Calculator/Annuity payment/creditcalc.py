# write your code here
from math import ceil, log


def get_input(message, type_cast=None):
    print(message)
    return type_cast(input()) if type_cast is not None else input()


def calc_period(months):
    return divmod(ceil(months), 12)  # years, months


def calc_nominal_interest_rate(interest):
    return interest / (12.0 * 100.0)


def calc_payment_number(interest_rate, credit_principal, monthly_payment):
    return log(
        monthly_payment / (monthly_payment - interest_rate * credit_principal),
        1 + interest_rate
    )


def calc_credit_principal(interest_rate, monthly_payment, payment_number):
    return monthly_payment / (
        interest_rate * pow(1 + interest_rate, payment_number) / (
            pow(1 + interest_rate, payment_number) - 1
        )
    )


def calc_monthly_payment(interest_rate, credit_principal, payment_number):
    return credit_principal * (
        interest_rate * pow(1 + interest_rate, payment_number) / (
            pow(1 + interest_rate, payment_number) - 1
        )
    )


def n_action():
    credit_principal = get_input("Enter credit principal:", int)
    monthly_payment = get_input("Enter monthly payment:", float)
    interest = get_input("Enter credit interest:", float)

    payment_number = calc_payment_number(
        calc_nominal_interest_rate(interest),
        credit_principal,
        monthly_payment
    )
    years, months = calc_period(payment_number)
    message = ""
    if years:
        message = f"{years} years"
    if months:
        message = (
            f"{message} and {months} months" if message else f"{months} months"
        )
    print(f"You need {message} to repay this credit!")


def a_action():
    credit_principal = get_input("Enter credit principal:", int)
    payment_number = get_input("Enter count of periods:", int)
    interest = get_input("Enter credit interest:", float)

    monthly_payment = calc_monthly_payment(
        calc_nominal_interest_rate(interest),
        credit_principal,
        payment_number
    )
    print(f"Your annuity payment = {ceil(monthly_payment)}!")


def p_action():
    monthly_payment = get_input("Enter monthly payment:", float)
    payment_number = get_input("Enter count of periods:", int)
    interest = get_input("Enter credit interest:", float)

    credit_principal = calc_credit_principal(
        calc_nominal_interest_rate(interest),
        monthly_payment,
        payment_number
    )
    print(f"Your credit principal = {round(credit_principal)}!")


actions = {
    "n": n_action,
    "a": a_action,
    "p": p_action,
}

action = get_input(
    "What do you want to calculate?\n"
    "type \"n\" - for count of months,\n" 
    "type \"a\" - for annuity monthly payment,\n"
    "type \"p\" - for credit principal:\n"
)
actions.get(action, (lambda principal: None))()
