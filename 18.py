f = open("18")

input = f.readlines()
input = map(lambda x:map(int, x.split()), input)

i = len(input)-2
while i>=0:
    for j in range(0, i+1):
        input[i][j] += max(input[i+1][j], input[i+1][j+1])
    i -= 1

print input[0][0]
