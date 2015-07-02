def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    retVal = ()
    for index in range(0, len(aTup), 2):
        retVal += (aTup[index],)
    return retVal
    
def oddTuples2(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    return aTup[::2]