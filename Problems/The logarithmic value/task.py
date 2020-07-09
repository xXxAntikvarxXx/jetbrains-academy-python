from math import log

value = int(input())
base = int(input())
print(round(log(value, base) if base > 1 else log(value), 2))
