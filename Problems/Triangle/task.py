n = int(input())
print("\n".join(
    ("#" * (2 * i + 1)).center(2 * (n - 1) + 1) for i in range(n)
))


# length = 2 * (n - 1) + 1
#
# for i in range(n):
#     print(("#" * (2 * i + 1)).center(length))
