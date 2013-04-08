from math import factorial

def t(n, i):
    _in = []
    for idx in range(i+1):
        _in.append(idx)
    
    out = []
    while i >= 0:
        if i > 0:
            cur = n / factorial(i)
            out.append(_in[cur])
            _in.pop(cur)
            n = n % factorial(i)
        else:
            out.append(_in[0])
        i -= 1
    print out

for i in range(120):
    t(i, 4)

t(999999, 9)
    
    

