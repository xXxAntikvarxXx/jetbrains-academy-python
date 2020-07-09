from math import sqrt


def area(a):
    return round(2 * sqrt(3) * pow(a, 2), 2)


def volume(a):
    return round(1 / 3 * sqrt(2) * pow(a, 3), 2)


edge = int(input())
print(area(edge), volume(edge))
