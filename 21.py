from math import floor
res = [0] * 10000

def put(ele, to):
    if ele < to:
        res[to] += ele
        
for i in range(1, 10000):
    j = i
    while i * j < 10000:
        if i==j:
            put(i, i*j)
        else:
            put(i, i*j)
            put(j, i*j)
        j += 1

count = 0        
for i in range(1, 10000):
    cur = res[i]
    if cur < 10000 and res[cur] == i and i != cur:
        print str(i) + " " + str(cur)
        count += cur
        count += i

print count / 2
