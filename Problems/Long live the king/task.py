x = int(input())
y = int(input())


MIN_X, MAX_X = 1, 8
MIN_Y, MAX_Y = 1, 8
STEPS = [-1, 0, 1]

print(sum(
    0 if i == 0 and j == 0 else 1
    for i in STEPS
    for j in STEPS
    if MIN_X <= x + i <= MAX_X and MIN_Y <= y + j <= MAX_Y
))


# Boolean solution
# c1 = 1 < int(input()) < 8
# c2 = 1 < int(input()) < 8
#
# print(8 if c1 and c2 else 5 if c1 ^ c2 else 3)

