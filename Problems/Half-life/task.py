# n = int(input().strip())
# r = int(input().strip())
#
# t = 0
# while n > r:
#     t += 12
#     n //= 2
# print(t)

n = int(input().strip())
r = int(input().strip())

t = 12
k = n // 2
while r < k:
    t += 12
    k //= 2
print(t)
