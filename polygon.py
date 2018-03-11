# find area and perimeter of a polygon
from math import *

def polysum(n, s):
    '''
    n, s: positive integers

    returns: positive integer, sum rounded to 4 decimal places
    '''
    area = 0.25*n*s**2/tan(pi/n)
    perimeter = s * n

    result = area + perimeter**2
    print(round(result,4))

polysum(75, 53)