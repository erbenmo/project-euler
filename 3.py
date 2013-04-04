from math import sqrt
from math import floor

def check(n):
    for i in range(2, int(floor(sqrt(n)))+1):
        if n % i == 0:
            return max(check(i), check(n/i))
    return n

number = 600851475143
print check(number)
