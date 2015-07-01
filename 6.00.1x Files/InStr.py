def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    strLength = len(aStr)
    if strLength == 0:
        return False
    elif strLength == 1:
        return aStr[0] == char
    else:
        mid = strLength/2
        if aStr[mid] == char:
            return True
        elif char < aStr[mid]:
            return isIn(char, aStr[:mid])
        else:
            return isIn(char, aStr[mid+1:])