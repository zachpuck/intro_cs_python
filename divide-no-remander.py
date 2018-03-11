def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''

    if a > b:
      test = b
    else:
      test = a
    
    if test == 1:
      return 1
    
    while test > 1:
      if b % test == 0 and a % test == 0:
        return test
      else:
        test -= 1
    
print(gcdIter(9, 12))