# TC-1 input variables
balance = 3329
annualInterestRate = 0.2

# TC-2 input variables
balance = 4773
annualInterestRate = 0.2

# TC-3 input variables
balance = 3926
annualInterestRate = 0.2

# Soltion # 1
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

# Soltion # 2

monthlyInterestRate = annualInterestRate/12
minPay = 0

balanceCopy = balance
while balance > 0:
    balance = balanceCopy
    minPay += 10
    for i in range(12):
        monthlyUnpaid = balance - minPay
        balance = monthlyUnpaid + monthlyInterestRate*monthlyUnpaid
print "Lowest Payment: "+str(round(minPay,2))
      

Test results