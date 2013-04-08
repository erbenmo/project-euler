a = 1
b = 1

print a
print 10**99
for i in range(1000):
    if b >= 10**(99):
        print b
        break
    a, b = b, a+b
