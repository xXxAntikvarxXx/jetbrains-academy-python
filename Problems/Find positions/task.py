# put your python code here
numbers = list(map(int, input().split()))
number = int(input())

print(" ".join(
    str(ind) for ind, num in enumerate(numbers) if number == num
) if number in numbers else "not found")
