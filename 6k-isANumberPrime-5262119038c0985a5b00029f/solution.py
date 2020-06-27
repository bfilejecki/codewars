import math

first_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

def is_prime(num):
    if num < 2:
        return False
    if num in first_primes:
        return True
    elif num < 101:
        return False

    for p in first_primes:
        if num%p == 0:
            return False

    for i in range(101, int(math.sqrt(num))+1):
        if num%i == 0:
            return False

    return True

