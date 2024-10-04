import math
from functools import reduce

def find_gcd_of_list(arr):
    return reduce(math.gcd, arr)

def find_divisors(n):
    divisors = []
    for i in range(2, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def common_divisors(arr):
    gcd_value = find_gcd_of_list(arr)
    return find_divisors(gcd_value)

arr = [42, 12, 18]
result = common_divisors(arr)
print(result)
