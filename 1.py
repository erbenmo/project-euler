def isMultiple(n):
    return n % 3 == 0 or n % 5 == 0

result = 0
for i in range(1000):
    if isMultiple(i):
        result += i

print result





        
    
