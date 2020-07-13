def is_prime(number):
    for n in range(2, int(number / 2) + 1):
        if number % n == 0:
            return False
    return True


prime_numbers = [
    number for number in range(2, 1001) if is_prime(number)
]
