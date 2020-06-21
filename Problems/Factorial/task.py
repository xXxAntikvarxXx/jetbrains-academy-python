n = int(input().strip())

if n == 0:
    print(1)

fact = 1

while n > 0:
    fact *= n
    n -= 1

print(fact)
