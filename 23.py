divsum = [0] * 28124

def put(ele, to):
    if ele < to:
        divsum[to] += ele
        
for i in range(1, 28124):
    j = i
    while i * j < 28124:
        if i==j:
            put(i, i*j)
        else:
            put(i, i*j)
            put(j, i*j)
        j += 1

abundants = []        
for i in range(1, 28124):
    if divsum[i] > i:
        abundants.append(i)

# print abundants        

isSum = [False]*28124
for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        if abundants[i] + abundants[j] < 28124:
            isSum[abundants[i] + abundants[j]] = True

i = 28123
count = 0
while i>0:
    if not isSum[i]:
        count += i
    i -= 1
print count
