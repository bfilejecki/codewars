def rot13(msg):
    return ''.join([rot13_char(c) for c in msg])

def rot13_char(char):
    if not char.isalpha():
        return char
    base = 65 if char.isupper() else 97 
    return chr((ord(char) + 13 - base) % 26 + base)

print([ord(s) for s in "test"])
print([ord(s) for s in rot13('test')])

