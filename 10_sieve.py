from math import floor, sqrt

big = 2000000
result = [True]*big
result[0] = result[1] = False

for i in range(2, int(floor(sqrt(big))+1)):
    j = i
    while i*j < big:
        result[i*j] = False
        j += 1

sum = 0        
for i in range(big):
    if result[i]:
        sum += i

print sum
