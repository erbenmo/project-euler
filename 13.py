f = open("13")

lines = f.readlines()
input = map(int, lines)

result = 0
for i in range(100):
    cur = input[i]
    result += cur

print result    
