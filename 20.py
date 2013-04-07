from math import factorial

x = factorial(100)

str = str(x)

count = 0
for s in str:
    count += int(s)

print count    
