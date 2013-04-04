answer = [0]*20

def split(n):
    cur = [0]*20
    while n > 1:
        for i in [2,3,5,7,11,13,17,19]:
            if n % i == 0:
                n /= i
                cur[i-1] += 1
                break
    for i in range(20):
        answer[i] = max(answer[i], cur[i])


for i in range(2, 21):
    split(i)

print [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print answer

result = 1
for i in range(20):
    if(answer[i] > 0):
        print answer[i]
        print i+1
        result *= ((i + 1)**(answer[i]))

print result   
