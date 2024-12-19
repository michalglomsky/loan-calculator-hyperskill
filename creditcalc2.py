# importing math module
import math

# taking the loan principal from input
loan_principal = int(input('Enter the loan principal:\n> '))

# user's prompt to calculate monthly payment or months to repay
what_to_calculate = input('What do you want to calculate?\n'
                          'type "m" for number of monthly payments,\n'
                          'type "p" for the monthly payment:\n> ')

# initializing variables of monthly payment and months to repay
monthly_payment = 0
months_to_repay = 0

# user asks to calculate one of the variables and inputs the other

# user wants to calculate the number of months to pay for a given fixed monthly payment
if what_to_calculate == "m":
    monthly_payment = int(input('Enter the monthly payment:\n> '))
    months_to_repay = math.ceil(loan_principal / monthly_payment)
    if months_to_repay == 1:
        print('It will take 1 month to repay the loan')
    else:
        print(f'It will take {months_to_repay} months to repay the loan')

# user wants to calculate monthly payment for a given number of periods
else:
    months_to_repay = int(input('Enter the number of months:\n> '))
    monthly_payment = math.ceil(loan_principal / months_to_repay)
    if (loan_principal % months_to_repay) == 0:
        print(f'Your monthly payment = {monthly_payment}')
    else:
        last_payment = loan_principal - (months_to_repay- 1) * monthly_payment
        print(f'Your monthly payment = {monthly_payment} and the last payment = {last_payment}.')
