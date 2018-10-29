def efficient(target_prime, verbose=False):
    n = 3
    i = 0
    while True:
        isPrime = True
        for j in range(2,n):
            if n % j == 0:
                isPrime = False
                break
        if isPrime == True:
            i += 1
            l = n
        if i == target_prime-1:
            return(n)
        if verbose == True and n % 1000 == 0:
            print('Current N: %i\t# of primes found: %i\tLatest prime: %i' % (n, i,l))
        n += 1

if __name__ == '__main__':
    print(efficient(10001, verbose=True))
