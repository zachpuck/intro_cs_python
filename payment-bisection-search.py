#29157.09
balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12
low = balance/12
high = (balance*(1 + monthlyInterestRate)**12)/12.0
originalBalance = balance
epsilon = 0.01

while abs(balance) > epsilon:
    balance = originalBalance
    payment = (low+high)/2
    
    for month in range(12):
        balance -= payment
        balance *= 1 + monthlyInterestRate
    
    if balance > 0:
        low = payment
    else:
        high = payment

print('Lowest Payment: ', round(payment, 2))
