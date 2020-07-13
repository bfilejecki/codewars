import re

def dirReduc(arr):
    directions_chain = ' '.join(arr)
    simplified_directions = simplify_string(directions_chain)
    return [x for x in simplified_directions.split(' ') if x]


def simplify_string(string):
    directions_pattern = re.compile(r'(NORTH\ +SOUTH)|(SOUTH\ +NORTH)|(EAST\ +WEST)|(WEST\ +EAST)')
    simplified_string = directions_pattern.sub('', string)
    if simplified_string == string:
        return simplified_string
    return simplify_string(simplified_string)

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a))
u=["NORTH", "WEST", "SOUTH", "EAST"]
print(dirReduc(u))