# For this task we can use this formula (k * (k + 1)) // 2 without loop
k = int(input().strip())

s = 0
while k > 0:
    s += k
    k -= 1
print(s)
