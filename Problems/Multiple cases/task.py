def f1(x):
    return x ** 2 + 1


def f2(x):
    return 1.0 / (x ** 2)


def f3(x):
    return x ** 2 - 1


def f(x):
    if x <= 0:
        return f1(x)
    if 0 < x < 1:
        return f2(x)
    return f3(x)
