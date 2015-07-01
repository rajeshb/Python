hi = 100
low = 0
print "Please think of a number between 0 and 100!"

while True:
    mid = (hi+low)/2
    print("Is your secret number " + str(mid) + "?")
    x = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if x == 'c':
        break
    elif x == 'h':
        hi = mid
    elif x == 'l':
        low = mid        
        mid = int((hi+low)/2)
    else:
        print("Sorry, I did not understand your input.")
print('Game over. Your secret number was: ' + str(mid))