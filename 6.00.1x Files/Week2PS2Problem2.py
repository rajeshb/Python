# TC-1 input variables
balance = 3329
annualInterestRate = 0.2

# TC-2 input variables
balance = 4773
annualInterestRate = 0.2

# TC-3 input variables
balance = 3926
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12
monthlyPayment = 0
currentBalance = balance

while currentBalance > 0:
    
    # increase monthly payment by 10 and check to see if the balance becomes 0
    monthlyPayment += 10
    
    for month in range(12):
        unpaidBalance = currentBalance - monthlyPayment
        currentBalance = unpaidBalance + unpaidBalance * monthlyInterestRate

    if currentBalance <= 0:
        break
    else:
        currentBalance = balance

print "Lowest Payment: " + str(monthlyPayment)