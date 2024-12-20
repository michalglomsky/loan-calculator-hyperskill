# importing math module
import math
import argparse

# creating parser
parser = argparse. ArgumentParser()



# adding arguments to parser
parser.add_argument("--payment", type=float, help="The payment amount per period")
parser.add_argument("--principal", type=float, help="The loan principal")
parser.add_argument("--periods", type=int, help="The number of months needed to repay the loan")
parser.add_argument("--interest", type=float, help="Annual interest rate (as a percentage)")

# collecting the arguments from the console
args = parser. parse_args()

# calculator function
def credit_calculator(arguments):
    # Defining variables for the formulas to calculate what's needed
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
        return f"Your loan principal = {round(p)}!"
    elif a is None:
        # formula for annuity payment
        a = p * ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
        return f"Your monthly payment = {math.ceil(a)}"
    elif n is None:
        # formula for number of months to pay the loan
        n = math.log(a / (a - (i * p)), 1+i)
        # rounding up number of months
        n = math.ceil(n)
        # adjusting the output based on the number of months
        if n < 12:
            return f"It will take {int(n)} months to repay this loan!"
        elif n % 12 == 0:
            n = n / 12
            return f"It will take {int(n)} years to repay this loan!"
        else:
            remainder = n % 12
            n = (n - remainder) / 12
            return f"It will take {int(n)} years and {int(remainder)} months to repay this loan!"
print(credit_calculator(args))