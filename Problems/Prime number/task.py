def is_prime(number):
    return number > 1 and any(
        number % i == 0
        for i in range(2, int(number / 2) + 1)
    ) is not True


# def is_prime_2(number):
#     for i in range(2, int(number / 2) + 1):
#         if number % i == 0:
#             return False
#     return number > 1

n = int(input())
print(f"This number {is_prime(n) and 'is' or 'is not'} prime")
