x = 0
n = 2

while x != 10001:
    isPrime = True
    for i in range(2,n+1):
        if n % i == 0:
            isPrime = False
            break
    n += 1
    if isPrime == True:
        x += 1
    if n % 100 == 0:
        print(n, x)

print(n, x)
