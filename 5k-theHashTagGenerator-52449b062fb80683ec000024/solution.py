import re

def generate_hashtag(s):
    if not s or len(s) == 0:
        return False
    s =  '#' + ''.join(x.capitalize() for x in s.split(' '))
    if len(s) > 140:
        return False
    return s

print(generate_hashtag('Codewars Is Nice'))
print(generate_hashtag('codewars is nice'))