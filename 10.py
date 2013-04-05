from math import sqrt, floor

def isPrime(n):
    for i in range(2, int(floor(sqrt(n)))+1):
        if n % i == 0:
            return False
    return True

sum = 2
i = 3
while i < 2000000:
    if isPrime(i):
     #   print i
        sum += i
    i+=2

print sum
