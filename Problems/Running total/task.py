numbers = list(map(int, input()))
numbers = [sum(numbers[:i + 1]) for i in range(len(numbers))]
print(numbers)
