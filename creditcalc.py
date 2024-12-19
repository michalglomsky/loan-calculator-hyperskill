# write your code here

# taking the loan principal from input
loan_principal = int(input("Enter the loan principal:\n> "))

# taking the monthly payment from input
monthly_payment = int(input("Enter the monthly payment:\n> "))

# calculating number of months to repay the loan
months_to_repay = int(loan_principal / monthly_payment)

print(f"It will take {months_to_repay} months to repay the loan")