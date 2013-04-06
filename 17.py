_f = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
_s = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


count = 0

fcount = 0
for i in range(1, 10):
    fcount += len(_f[i])

# 1 - 19
for i in range(1, 20):
    count += len(_f[i])

# 20 - 99
for i in range(2, 10):
    count += (len(_s[i]) * 10 + fcount)

# 1 - 99    
tcount = count
    
# 100 - 999
for i in range(1, 10):
    count += 100 * (len(_f[i]) + len("hundred"))
    count += 99 * len("and")
    count += tcount

count += len("onethousand")


print count


def one(n):
    assert n>=0 and n<=19
    return _f[n]

def ten(n):
    assert n>=20 and n<=99
    a, b = n/10, n%10
    return _s[a] + " " + one(b)

def hundred(n):
    assert n>=100 and n<=999
    a, b = n / 100, n % 100
    ret = _f[a] + " hundred"
    if b > 0:
        ret += " and "
    if b >= 0 and b <= 19:
        ret += one(b)
    else:
        ret += ten(b)
    return ret

count = 0
for i in range(1, 20):
    s = one(i)
    s = s.replace(" ", "")
    print s
    count += len(s)
for i in range(20, 100):
    s = ten(i)
    s = s.replace(" ", "")
    print s
    count += len(s)

for i in range(100, 1000):
    s = hundred(i)
    s = s.replace(" ", "")
    print s
    count += len(s)

s = "one thousand"
s = s.replace(" ", "")
print s
count += len(s)
print count
