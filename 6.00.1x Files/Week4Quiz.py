def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    
    if x < b:
        return 0
    elif x == b:
        return 1

    return myLog(x/b, b) + 1
    
def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    retList = []
    for item in aList:
        if len(item) < 4:
            retList.append(item)
    return retList
    
def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # return N, if single digit
    if N / 10 <= 0:
        return N
    
    return N%10 + sumDigits(N/10)
    
def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    retList = []
    for key in aDict.keys():
        if aDict[key] == target:
            retList.append(key)
    return sorted(retList)
    
def f(s):
    return 'a' in s
    
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    arrLen = len(L)
    for i in range(arrLen, 0, -1):
        if not f(L[i-1]):
            del L[i-1]
    return len(L)

#run_satisfiesF(L, satisfiesF)