# a<500
# b<500
# a+b>500
# a>b


for a in range(1, 500):
    b_min = 501-a
    for b in range(b_min, a):
        c = 1000-a-b
        if a**2+b**2 == c**2:
            print a, b, c
            print a*b*c
            break
