from random import randint

def digital_root(n):
    if (len(str(n))) < 2:
        return n
    else:
        new_num = sum(digitize(n))
        return digital_root(new_num)

def digitize(n):
    digits = []
    for _ in range(len(str(n))):
        digit = n%10
        n = n // 10
        digits.append(digit)
    digits.reverse()
    return digits

print(digitize(55555555555555555555555))
