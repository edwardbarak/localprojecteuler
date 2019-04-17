class divisibleTriangle(target):
    def __init__(self, target):
        self.target = target
    def findTarget(self):
         

# start with i=1, count divisors for i using: [sum(range(0,i+1)) % j for j in range(0,sum(range(0,i+1))]
# if divisor count < target, lowerBound = i, i*=10, count divisors for i
# elif divisor count >= target, upperBound = i, count divisors starting at lowerBound with step=1
# return first number to have divisor 

if __name__ == '__main__':
    from sys import argv
    dt = divisibleTriangle(argv[0])
    print(dt.findTarget())
