# calculating the remaining balance of a credit card after paying only minimum required for 12 months
def calBalance(balance, annualInterestRate, monthlyPaymentRate):
    month = 12
    newBalance = balance

    while month > 0:
        month -= 1
        currentBalance = newBalance - (monthlyPaymentRate * newBalance)
        newBalance = currentBalance + (annualInterestRate/12.0 * currentBalance)

    print('Remaining balance: ', round(newBalance, 2))

calBalance(42, 0.2, 0.04)