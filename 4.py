def isPalindrome(n):
    str_n = str(n)
    return str_n == str_n[::-1]

largest = -1
for i in range(1, 1000):
    for j in range(i, 1000):
        if isPalindrome(i*j) and i * j > largest:
            largest = i * j
print largest
