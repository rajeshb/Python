def gcdIter(a,b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    minVal = min(a,b)
    
    while (a % minVal != 0 or b % minVal != 0):
        minVal -= 1
    return minVal

## Euclidean algorithm, or Euclid's algorithm
##
def gcdRecur(a,b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    
    if a == 0:
        return b
    return gcdRecur(b % a, a)