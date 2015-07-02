def howMany(aDict):
    count = 0
    for value in aDict.values():
        for e in value:
            count += 1
    return count


def howMany1(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for value in aDict.values():
        # Since all the values of aDict are lists, aDict.values() will 
        #  be a list of lists
        result += len(value)
    return result

def howMany2(aDict):
    '''
    Another way to solve the problem.

    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for key in aDict.keys():
        result += len(aDict[key])
    return result

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    retKey = None
    retKeyLen = 0
    for key in aDict.keys():
        if len(aDict[key]) >= retKeyLen:
            retKey = key
            retKeyLen = len(aDict[key])
    return retKey