def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    result = ()
    for i in range(0, len(aTup), 2):
        result = result + (aTup[i],)
        
    print(result)
    
myTuple = ('I', 'am', 'a', 'test', 'tuple')
oddTuples(myTuple)