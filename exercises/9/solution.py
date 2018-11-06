from math import pow
from itertools import product
from numpy import prod

aRange = range(1,322+1)
bRange = range(2,499+1)
cRange = range(335, 997+1)

cartesianProduct = product(aRange, bRange, cRange)

sum1k = [i for i in cartesianProduct if pow(i[0],2) + pow(i[1],2) == pow(i[2],2) and i[0]+i[1]+i[2] == 1000]

print(prod(list(sum1k[0])))
