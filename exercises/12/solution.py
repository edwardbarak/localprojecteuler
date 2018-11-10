def firstTriDivisors(target, log_step=10):
    lowerBound = 1
    upperBound = log_step
    pass

# start with i=1, count divisors for i using: [sum(range(0,i+1)) % j for j in range(0,sum(range(0,i+1))]
# if divisor count < target, lowerBound = i, i*=10, count divisors for i
# elif divisor count >= target, upperBound = i, count divisors starting at lowerBound with step=1
# return first number to have divisor 
