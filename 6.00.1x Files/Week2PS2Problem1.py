# TC-1 input variables
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# TC-2 input variables
#balance = 4842
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04

monthlyPayment = 0.0
currentBalance = balance
monthlyInterestRate = annualInterestRate / 12
totalPaid = 0.0

# Asked to use round() for 2 digit decimal output
# %.2f would be ideal for printing 2 digits
# Example, 19.20323 would be 19.2 using round, 19.20 using format option

for month in range(12):
    print "Month: " + str(month+1)
    monthlyPayment = currentBalance * monthlyPaymentRate
    totalPaid += monthlyPayment
    unpaidBalance = currentBalance - monthlyPayment
    currentBalance = unpaidBalance + unpaidBalance * monthlyInterestRate
    print "Minimum monthly payment: " + str(round(monthlyPayment,2))
    print "Remaining balance: " + str(round(currentBalance,2))
print "Total paid: " + str(round(totalPaid,2))
print "Remaining Balance: " + str(round(currentBalance,2))
