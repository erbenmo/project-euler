hash = {1 : 1}

def rec(n):
    if n in hash:
        return hash[n]

    if n%2 == 0:
        hash[n] = 1 + rec(n/2)
    else:
        hash[n] = 1 + rec(3*n+1)

    return hash[n]



largest = 0
idx = -1
for i in range(2, 1000000):
    cur = rec(i)
    if largest < cur:
        largest = cur
        idx = i

print idx

