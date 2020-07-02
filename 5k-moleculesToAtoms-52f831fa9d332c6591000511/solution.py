import re

def parse_molecule (formula):
    pass
   
   
def parse_simple_molecule(formula):
    elements_count = {}
    simple_molecule_regex = re.compile(r'([A-Z]{1}[a-z]?)([0-9]*)')

    matches = simple_molecule_regex.findall(formula)
    for match in matches:
        element = match[0]
        quantity = int(match[1]) if match[1] else 1
        if element:
            elements_count[element] = elements_count[element] + quantity if element in elements_count else quantity

    return elements_count

def multiply_molecule(elements_count, quantity):
    return {k:v*quantity for k,v in elements_count.items()}

print(parse_simple_molecule("H2O"))
print(multiply_molecule(parse_simple_molecule("H2O"), 2))
print(parse_simple_molecule("H2O12"))
print(parse_molecule("Mg(OH)2"))
print(parse_molecule("K4[ON(SO3)2]2"))