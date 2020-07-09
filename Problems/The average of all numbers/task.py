# put your python code here
a = int(input())
b = int(input())
n = 3

# Without for loop
# print((a + (-a % n) + b - (b % n)) / 2.0)

# With for loop
numbers = [number for number in range(a, b + 1) if number % n == 0]
print(sum(numbers) / len(numbers))
