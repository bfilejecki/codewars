import re


def parse_molecule(formula):
    formula = replace_brackets(formula)
    simplified_formula = simplify_formula(formula)

    return parse_simple_molecule(simplified_formula)


def simplify_formula(formula):
    result = formula
    last_opened_bracket_pos = None
    for i, char in enumerate(formula):
        if char == '(':
            last_opened_bracket_pos = i
        elif char == ')':
            complex_formula_regex = re.compile(r'[(]([^(]\w*)[)]([0-9]*)')
            complex_part_match = complex_formula_regex.match(
                result, last_opened_bracket_pos)
            complex_part = complex_part_match.group(1)
            multiplier = int(complex_part_match.group(2)) if complex_part_match.group(2) else 1
            simplified_part = multiply_formula_elements(parse_simple_molecule(complex_part), multiplier)
            result = result[:complex_part_match.start()] + simplified_part + result[complex_part_match.end():]
            return simplify_formula(result)

    return result


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


def replace_brackets(string):
    string = re.sub(r'[[{]', '(', string)
    string = re.sub(r'[]}]', ')', string)
    return string


def multiply_formula_elements(elements_count, quantity):
    if quantity < 2:
        return convert_elements_to_formula(elements_count)
    multiplied_elements_count = {
        k: v*quantity for k, v in elements_count.items()}

    return convert_elements_to_formula(multiplied_elements_count)


def convert_elements_to_formula(elements_count):
    return ''.join([f'{k}{v}' for k, v in elements_count.items()])

#print(parse_molecule('Mg(OH)2'))
#print(parse_molecule("Mg(OH)2"))
#print(parse_molecule("K4[ON(SO3)2]2"))
print(parse_molecule('K2(OH)2(OH2)(OH3)2'))
