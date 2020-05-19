from math import sqrt
import numpy as np

def triangle_generator():
    """
    The sequence of triangle numbers is generated by adding the natural numbers. 
    So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The
     first ten terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
    """
    n = 0
    lastTriangle = 0
    while True:
        n += 1
        lastTriangle += n
        yield (n, lastTriangle)


def count_factors(triangle):
    """Counts the number of factors a number has"""
    squareRoot = sqrt(triangle)
    tests = np.arange(1, int(squareRoot + 1))                       # generate half of possible factors
    tests = triangle % tests                                        # test generated list for actual factors
    factorsCnt = (len(tests) - len(np.extract(tests, tests))) * 2   # evaluate test as booleans, count # of 0's
    if not triangle % sqrt(triangle): factorsCnt -= 1               # make sure to not double count perfect square factor, like double counting 6 for 36
    return factorsCnt

def first_triangle_with_gt_n_factors(n):
    gen = triangle_generator()
    factors = 0
    while factors < n:
        temp = gen.__next__()
        factors = count_factors(temp[1])
        # print('n: {}\ttri: {}\tfactors: {}'.format(temp[0], temp[1], factors))    # For debugging
    
    # suffix logic
    tail = str(temp[1])[-2:]
    if tail[-1] == '1' and tail != '11': suffix = 'st'
    elif tail[-1] == '2' and tail != '12': suffix = 'nd'
    elif tail[-1] == '3' and tail != '13': suffix = 'rd'
    else: suffix = 'th'

    print('The {pos}{suffix} triangle, with a value of {value}, has {factors} factors.'.format(pos=temp[0], suffix=suffix, value=temp[1], factors=factors))

if __name__ == "__main__":
    first_triangle_with_gt_n_factors(500)