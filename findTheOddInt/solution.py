def find_it(seq):
    numbers = {}
    scanNumbers = (x for x in seq)
    for x in scanNumbers:
        if x in numbers:
            numbers[x] = numbers[x] + 1
        else:
            numbers[x] = 1
    it = next((k, v) for k, v in numbers.items() if v & 1)
    return it[0]


print(find_it([20,1,1]))