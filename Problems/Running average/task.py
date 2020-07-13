numbers = list(map(int, input()))
# print([
#     (numbers[i] + numbers[i + 1]) / 2.0
#     for i in range(0, len(numbers))
#     if i < len(numbers) - 1
# ])
print([
    (numbers[i] + numbers[i + 1]) / 2.0
    for i in range(0, len(numbers) - 1)
])
