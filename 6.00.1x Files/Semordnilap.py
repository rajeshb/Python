def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    str2Len = len(str2)
    str1Len = len(str1)
    
    if str1Len != str2Len:
        return False
        
    if str1Len == 1:
        return str1[0] == str2[str2Len-1]
        
    if str1[0] != str2[str2Len-1]:
        return False
        
    return semordnilap(str1[1:], str2[:str2Len-1])
    
def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)
