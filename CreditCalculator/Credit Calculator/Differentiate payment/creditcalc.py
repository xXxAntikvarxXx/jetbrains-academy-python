# write your code here
from argparse import ArgumentParser
from math import ceil, log, floor


def build_parser():
    parser = ArgumentParser()
    parser.add_argument("--type", type=str, choices=[
        "annuity", "diff"
    ], required=False, default=None)
    parser.add_argument("--payment", type=int, required=False, default=None)
    parser.add_argument("--principal", type=int, required=False, default=None)
    parser.add_argument("--periods", type=int, required=False, default=None)
    parser.add_argument("--interest", type=float, required=False, default=None)
    return parser


def args_validation(args):
    if (
        args.type is None or
        (args.type == "diff" and (
            args.payment is not None or
            (
                (args.principal is not None and args.principal < 0) or
                (args.payment is not None and args.payment < 0) or
                (args.periods is not None and args.periods < 0)
            )
        )) or
        (args.type == "annuity" and (
            args.interest is None or
            (args.periods is None and args.payment is None) or
            (args.periods is None and args.principal is None) or
            (args.payment is None and args.principal is None)
        ))
    ):
        print("Incorrect parameters.")
    else:
        return args


def calc_nominal_interest_rate(interest):
    return interest / (12.0 * 100.0)


def calc_diff_month_payment(month, interest_rate, credit_principal, period):
    return ceil(credit_principal / period + interest_rate * (
        credit_principal - (credit_principal * (month - 1)) / period
    ))


def calc_overpayment(diff_month_payments, credit_principal):
    return sum(diff_month_payments) - credit_principal


def calc_monthly_payment(interest_rate, credit_principal, period):
    return ceil(credit_principal * (
        interest_rate * pow(1 + interest_rate, period) / (
            pow(1 + interest_rate, period) - 1
        )
    ))


def calc_credit_principal(interest_rate, monthly_payment, period):
    return floor(monthly_payment / (
        interest_rate * pow(1 + interest_rate, period) / (
            pow(1 + interest_rate, period) - 1
        )
    ))


def calc_period(months):
    return divmod(ceil(months), 12)  # years, months


def calc_payment_number(interest_rate, credit_principal, monthly_payment):
    return log(
        monthly_payment / (monthly_payment - interest_rate * credit_principal),
        1 + interest_rate
    )


def diff(args):
    interest_rate = calc_nominal_interest_rate(args.interest)
    diff_month_payments = []
    for month in range(1, args.periods + 1):
        diff_month_payments.append(
            calc_diff_month_payment(
                month,
                interest_rate,
                args.principal,
                args.periods
            )
        )
        print(f"Month {month}: paid out {diff_month_payments[-1]}")
    print()
    overpayment = calc_overpayment(diff_month_payments, args.principal)
    print(f"Overpayment = {overpayment}")


def annuity(args):
    interest_rate = calc_nominal_interest_rate(args.interest)
    if args.principal is not None and args.periods is not None:
        monthly_payment = calc_monthly_payment(
            interest_rate,
            args.principal,
            args.periods
        )
        print(f"Your annuity payment = {monthly_payment}!")
        overpayment = calc_overpayment(
            [monthly_payment] * args.periods,
            args.principal
        )
        print(f"Overpayment = {overpayment}")
    elif args.payment is not None and args.periods is not None:
        credit_principal = calc_credit_principal(
            interest_rate,
            args.payment,
            args.periods
        )
        print(f"Your credit principal = {credit_principal}!")
        overpayment = calc_overpayment(
            [args.payment] * args.periods,
            credit_principal
        )
        print(f"Overpayment = {overpayment}")
    elif args.payment is not None and args.principal is not None:
        period = calc_payment_number(
            interest_rate,
            args.principal,
            args.payment
        )
        years, months = calc_period(period)
        message = ""
        if years:
            message = f"{years} years"
        if months:
            message = (
                f"{message} and {months} months"
                if message else
                f"{months} months"
            )
        print(f"You need {message} to repay this credit!")
        overpayment = calc_overpayment(
            [args.payment] * ceil(period),
            args.principal
        )
        print(f"Overpayment = {overpayment}")


actions = {
    "diff": diff,
    "annuity": annuity,
}


parser = build_parser()
args = args_validation(parser.parse_args())
if args is not None:
    actions[args.type](args)
