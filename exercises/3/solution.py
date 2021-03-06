# NOTE: This does not work if largest prime factor of n > 104729

def get_largest_prime_factor_of_n(n=600851475143):
    # import csv containing first 10,000 primes
    with open('primes.csv', 'r') as f:
        primes = f.read()
        f.close()

    primes = primes.split(',')                                                  # parse csv
    primes = [int(prime) for prime in primes]                                   # convert strings to ints
    isFactor = [n % prime == 0 for prime in primes]                             # determine if prime number is a factor of n
    factors = [pair[0] for pair in zip(primes, isFactor) if pair[1] == True]    # find all prime numbers that are factors of n

    return max(factors)                                                         # returns largest prime that is a factor of n

if __name__ == "__main__":
    print(get_largest_prime_factor_of_n())