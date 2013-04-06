def isLeap(n):
    if n %4 != 0:
        return False
    if n % 1000 != 0:
        return True
    if n % 400 == 0:
        return True
    return False

def len_month(m, y):
    if m in [4, 6, 9, 11]:
        return 30
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if isLeap(y):
        return 29
    else:
        return 28


# 0, 1, 2, 3, 4, 5, 6
# S, M, T, W, T, F, S


cur = 2
count = 0

for y in range(1901, 2001):
    for m in range(1, 13):
        if cur == 0:
            count += 1
        cur = (cur + len_month(m, y)) % 7

print count        
