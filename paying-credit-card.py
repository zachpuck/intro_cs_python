# calculating the remaining balance of a credit card after paying only minimum required for 12 months
def calBalance(balance, annualInterestRate, monthlyPaymentRate):
    month = 12
    newBalance = balance

    while month > 0:
        month -= 1
        currentBalance = newBalance - (monthlyPaymentRate * newBalance)
        newBalance = currentBalance + (annualInterestRate/12.0 * currentBalance)

    print('Remaining balance: ', round(newBalance, 2))

# calculate fixed monthly payment in order to pay off card in 12 months
def fixedPayment(balance, annualInterestRate):
    monthlyPayment = 10
    currentBalance = balance

    while currentBalance > 0:

        for month in range(12):
            currentBalance -= monthlyPayment
            interest = (annualInterestRate/12.0)*currentBalance
            currentBalance += interest
        if currentBalance > 0:
            currentBalance = balance
            monthlyPayment += 10

    print('Lowest Payment: ', monthlyPayment)

calBalance(42, 0.2, 0.04)
fixedPayment(3329, 0.2)