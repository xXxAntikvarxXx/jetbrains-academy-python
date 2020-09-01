def sq_sum(*numbers):
    return sum(map(
        (lambda number: number ** 2),
        numbers
    ))
