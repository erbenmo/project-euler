from math import sqrt, floor


def isPrime(n):
    for i in range(2, int(floor(sqrt(n)))+1):
        if n % i == 0:
            return False
    return True

i == 0
num = 2
while i != 10001:
    if isPrime(num):
        i += 1
    num += 1
