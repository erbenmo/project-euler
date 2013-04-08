f = open("22")
input = f.readline()
input = input.split(",")
input = map(lambda x: x.replace('"', ""), input)
input.sort()

result = 0

def score(str):
    score = 0
    for s in str:
        score += (ord(s) - ord('A') + 1)
    return score

for i in range(len(input)):
    result += (i+1) * score(input[i])

print result    
