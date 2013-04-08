a = 1
b = 1


i = 1
while True:
    if len(str(a)) == 1000:
        print a
        print i
        break
    a, b = b, a+b
    i += 1
