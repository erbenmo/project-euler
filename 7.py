from math import sqrt, floor, ceil


def isPrime(n):
    if n == 2:
        return True
    
    for i in range(2, int(floor(sqrt(n)))+1):
        if n % i == 0:
            return False
    return True

i = 1
num = 2
while True:
    if isPrime(num):
        print num
        if i == 10001:
            print num
            break
        i += 1
    num += 1
