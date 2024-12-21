# importing math module
import math
import argparse

# creating parser
parser = argparse. ArgumentParser()

# adding arguments to parser
parser.add_argument("--type", help="Choose between the type of your loan - annuity or differentiated")
parser.add_argument("--payment", type=float, help="The payment amount per period")
parser.add_argument("--principal", type=float, help="The loan principal")
parser.add_argument("--periods", type=int, help="The number of months needed to repay the loan")
parser.add_argument("--interest", type=float, help="Annual interest rate (as a percentage)")

# collecting the arguments from the console
args = parser. parse_args()

# annuity calculator function
def annuity_credit_calculator(arguments):
    # Defining variables for the formulas to calculate what's needed
    # months counter for the overpayment calculation
    months_counter = 1
    # annuity payment
    a = arguments.payment
    # nominal monthly interest rate
    i = arguments.interest / (12 * 100)
    # number of months to pay the loan
    n = arguments.periods
    # loan principal
    p = arguments.principal
    if arguments.interest is None:
        print("Error: You didn't specify the interest rate.\n"
              "You must enter the value of '--interest' as an interest rate argument")
    if p is None:
        # formula for loan principal
        p = a / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
        p = math.floor(p)
        print(f"Your loan principal = {p}!")
    elif a is None:
        # formula for annuity payment
        a = p * ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
        a = math.ceil(a)
        print(f"Your monthly payment = {a}")
    elif n is None:
        # formula for number of months to pay the loan
        n = math.log(a / (a - (i * p)), 1+i)
        # rounding up number of months
        n = math.ceil(n)
        # adjusting the output based on the number of months
        if n < 12:
            print(f"It will take {int(n)} months to repay this loan!")
        elif n % 12 == 0:
            years = n / 12
            print(f"It will take {int(years)} years to repay this loan!")
        else:
            remainder = n % 12
            years = (n - remainder) / 12
            print(f"It will take {int(years)} years and {int(remainder)} months to repay this loan!")
    # calculating overpayment
    overpayment = int(abs(p - (a * n)))
    print(f"Overpayment = {overpayment}")



# differentiated credit calculator
def diff_credit_calculator(arguments):
    # Defining variables for the formulas to calculate what's needed
    # months counter for loan calculation
    months_counter = 1
    # nominal monthly interest rate
    i = arguments.interest / (12 * 100)
    # number of months to pay the loan
    n = arguments.periods
    # loan principal
    p = arguments.principal
    # sum of all payments to calculate the overpayment
    sum_of_payments = 0
    while months_counter <= int(arguments.periods):
        payment = (p / n) + i * (p - (p * (months_counter-1) / n))
        payment = math.ceil(payment)
        sum_of_payments += payment
        print(f"Month {months_counter}: payment is {payment}")
        months_counter += 1
    overpayment = int(abs(p - sum_of_payments))
    print(f"\nOverpayment = {overpayment}")

# Check if any arguments are negative
def check_negative_arguments(arguments):
    for key, value in vars(arguments).items():
        if value is not None and isinstance(value, (int, float)) and value < 0:
            return True
    return False

# Check if fewer than 4 arguments were provided
def check_missing_arguments(arguments):
    required_params = ["type", "interest"]
    if arguments.type == "annuity" and arguments.payment is None and arguments.principal is None and arguments.periods is None:
        return True
    elif arguments.type == "diff" and (arguments.payment is not None or arguments.principal is None or arguments.periods is None):
        return True
    return False

# Run checks
if (
    args.type not in ["annuity", "diff"] or
    args.interest is None or
    check_negative_arguments(args) or
    check_missing_arguments(args)
):
    print("Incorrect parameters")
else:
    if args.type == "annuity":
        annuity_credit_calculator(args)
    elif args.type == "diff":
        diff_credit_calculator(args)