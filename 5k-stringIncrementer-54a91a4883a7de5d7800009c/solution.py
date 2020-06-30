import re

def increment_string(strng):
    match = re.search(r'^(.*[^\d]+)*(\d*)$', strng)

    name = match.groups()[0] if match.groups()[0] else ''
    counter_value_string = match.groups()[1] if match.groups()[1] else '0'

    return name + str(int(counter_value_string)+1).zfill(len(counter_value_string))


def increment_string_v2(strng):
    match = re.search(r'^(.*?)(\d+)$', strng)

    name, counter_value_string = (match.group(1), match.group(2)) if match else ('','0')

    return name + str(int(counter_value_string)+1).zfill(len(counter_value_string))

    
print(increment_string("var099"))
print(increment_string(""))
print(increment_string("#$%%"))
