# My solution

def order_weight(string):
    if string is None or len(string) == 0:
        return ""
    numbers = [int(x) for x in string.split(' ')]
    numbers_weights = [(x, sum(digitize(x))) for x in numbers]
    return ' '.join([str(x[0]) for x in sorted(numbers_weights, key=sort_by_weight)])

def digitize(num):
    digits = []
    for _ in range(len(str(num))):
        digits.append(num%10)
        num = num // 10

    digits.reverse()
    return digits


def sort_by_weight(item):
    return (item[1], str(item[0]))

# Best solution 
def weight_key(s):
    return (sum(int(c) for c in s), s)
def order_weight_v2(s):
    return ' '.join(sorted(s.split(' '), key=weight_key))


print(order_weight("103 123 4444 99 2000 101 11 1001"))
print(order_weight(""))