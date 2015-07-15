# TC-1 input variables
balance = 320000
annualInterestRate = 0.2

# TC-2 input variables
balance = 999999
annualInterestRate = 0.18

# Soltion 1
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

# Solution 2

balanceCopy = balance
monthlyInterestRate = annualInterestRate/12
payLowBound = balance/12.0
payHighBound = (balance*((1+monthlyInterestRate)**12))/12.0
minPay = 0

while balance > 0.02 or balance < -0.02:
    balance = balanceCopy
    minPay = (payLowBound + payHighBound)/2
    for i in range(12):
        monthlyUnpaid = balance - minPay
        balance = round(monthlyUnpaid + monthlyInterestRate*monthlyUnpaid,2)
    if balance > 0:
        payLowBound = minPay
    if balance < 0:
        payHighBound = minPay

print "Lowest Payment: "+str(round(minPay,2))
