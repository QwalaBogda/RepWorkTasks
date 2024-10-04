import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(min_value, max_value):
    primes = []
    for num in range(min_value, max_value + 1):
        if is_prime(num):
            primes.append(num)
    return primes

min_value = 11
max_value = 20
result = primes_in_range(min_value, max_value)
print(result)
