def primesBetween(end, start=2, verbose=False):
    primes = []
    for i in range(start,end+1):
        isPrime = True
        for j in primes:
            if i % j == 0:
                isPrime = False
                break
        if isPrime == True:
            primes.append(i)
        if i % 1000 == 0 and verbose==True:
            print('i:\t', i)
    return(sum(primes))

if __name__ == '__main__':
    print(primesBetween(2000000, verbose=True))
