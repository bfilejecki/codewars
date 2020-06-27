def solution(number):
    multipliers = (x for x in range(number) if not x%3 or not x%5)
    return sum(multipliers)

print(solution(10))
