def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '':
        return False

    m = len(aStr)//2

    if char == aStr[m]:
        return True
    elif char > aStr[m]:
        return isIn(char, aStr[(m+1):])
    else:
        return isIn(char, aStr[:m])
    
print(isIn('b', 'aabdejlmruuvv'))
