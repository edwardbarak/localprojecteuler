from math import sqrt
import numpy as np

def triangle_generator():
    n = 0
    lastTriangle = 0
    while True:
        n += 1
        lastTriangle += n
        yield (n, lastTriangle)


def count_factors(triangle):
    squareRoot = sqrt(triangle)
    tests = np.arange(1, int(squareRoot + 1))
    tests = triangle % tests
    factorsCnt = (len(tests) - len(np.extract(tests, tests))) * 2
    if not triangle % sqrt(triangle): factorsCnt -= 1
    return factorsCnt

def first_triangle_with_gt_n_factors(n):
    gen = triangle_generator()
    factors = 0
    while factors < n:
        temp = gen.__next__()
        factors = count_factors(temp[1])
        print('n: {}\ttri: {}\tfactors: {}'.format(temp[0], temp[1], factors))

if __name__ == "__main__":
    first_triangle_with_gt_n_factors(500)