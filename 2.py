limit = 4000000

a = 1
b = 2
result = 0

while b < limit:
    if b % 2 == 0:
        result += b
    a, b = b, a + b

print result
