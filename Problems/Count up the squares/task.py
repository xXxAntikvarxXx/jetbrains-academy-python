# put your python code here
numbers = []

while len(numbers) == 0 or sum(numbers) != 0:
    numbers.append(int(input()))

print(sum(map((lambda x: x * x), numbers)))
