from math import pow

# variables
start = 1
end = 100

sum_of_squares = sum([pow(i,2) for i in range(start,end+1)])
square_of_sums = pow(sum(range(start,end+1)), 2)

print(square_of_sums - sum_of_squares)
