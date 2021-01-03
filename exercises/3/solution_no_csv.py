def sieve(end):
    potentialPrimes = set(range(2, end+1))
    primes = []
    i = next(iter(potentialPrimes))

    while i**2 < end:
        primes.append(i)
        potentialPrimes = potentialPrimes.difference(set(range(i, end+1, i)))
        i = next(iter(potentialPrimes))
    return primes + list(potentialPrimes)

def get_largest_prime_factor_of_n(n):
    primes = sieve(n-1).reverse()
    for prime in primes:
        if n % prime == 0: return prime
    return None

if __name__ == "__main__":
    # print(get_largest_prime_factor_of_n(600851475143))
    print(len(sieve(600851475143)))