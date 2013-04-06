f = open("11")
lines = f.readlines()

input = [[0]*20]*20

for i in range(20):
    line = lines[i]
    temp = line.split()
    arr = map(int, temp)
    input[i] = arr

largest = 0
for i in range(20):
    for j in range(20):
        if j+3 < 20:
            largest = max(largest, input[i][j] * input[i][j+1] * input[i][j+2] * input[i][j+3])
        if i+3 < 20:
            largest = max(largest, input[i][j] * input[i+1][j] * input[i+2][j] * input[i+3][j])
        if i+3 < 20 and j+3 < 20:
            largest = max(largest, input[i][j] * input[i+1][j+1] * input[i+2][j+2] * input[i+3][j+3])
        if i+3 < 20 and j-3 >= 0:
            largest = max(largest, input[i][j] * input[i+1][j-1] * input[i+2][j-2] * input[i+3][j-3])

print largest            
