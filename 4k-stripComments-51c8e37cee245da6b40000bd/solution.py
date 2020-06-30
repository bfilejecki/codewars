import re

def solution(string,markers):
    stripped_lines = []
    for line in string.split('\n'):
        for marker in markers:
            line = re.sub(rf'\s*[{marker}].*$','', line)
        stripped_lines.append(line)
    return '\n'.join(stripped_lines)

def solution_v2(string,markers):
    stripped_lines = []
    for line in string.split('\n'):
        for marker in markers:
            index = line.index(marker) if marker in line else None
            line = line[:index] if index is not None else line
        stripped_lines.append(line.strip())
    return '\n'.join(stripped_lines)

print('\n'.join(['', '', '']))

print(solution_v2(". pears\ncherries bananas apples\navocados strawberries\nwatermelons # bananas cherries cherries\n, oranges # apples avocados", ['!', "'", '=', '@', ',', '^']))
print(". pears\ncherries bananas apples\navocados strawberries\nwatermelons # bananas cherries cherries\n, oranges # apples avocados' should equal '. pears\ncherries bananas apples\navocados strawberries\nwatermelons # bananas cherries cherries\n")