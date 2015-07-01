# TC-1 input variables
balance = 320000
annualInterestRate = 0.2

# TC-2 input variables
balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12
currentBalance = balance
monthlyPaymentLB = currentBalance/12
monthlyPaymentUB = (currentBalance * (1+monthlyInterestRate)**12)/12.0
monthlyPayment = 0.0

while currentBalance > 0:
    
    monthlyPayment = (monthlyPaymentLB + monthlyPaymentUB) / 2
    
    for month in range(12):
        unpaidBalance = currentBalance - monthlyPayment
        currentBalance = unpaidBalance + unpaidBalance * monthlyInterestRate

    if abs(currentBalance) <= 0.01:
        break
    else:
        if currentBalance > 0:
            monthlyPaymentLB = monthlyPayment
        else:
            monthlyPaymentUB = monthlyPayment
        currentBalance = balance

print "Lowest Payment: " + str(round(monthlyPayment,2))