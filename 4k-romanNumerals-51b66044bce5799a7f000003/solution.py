class RomanNumerals:

    roman_decimal_map = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    decimal_roman_map = {
        9: ('', 'CM', 'XC', 'IX'),
        8: ('', 'DCCC', 'LXXX', 'VIII'),
        7: ('', 'DCC', 'LXX', 'VII'),
        6: ('', 'DC', 'LX', 'VI'),
        5: ('', 'D', 'L', 'V'),
        4: ('', 'CD', 'XL', 'IV'),
        3: ('', 'CCC', 'XXX', 'III'),
        2: ('', 'CC', 'XX', 'II'),
        1: ('', 'C', 'X', 'I'),
        0: ('', '', '', '')
    }

    decimal_roman_map = {
        9: ('IX', 'XC', 'CM', ''),
        8: ('VIII',  'LXXX', 'DCCC', ''),
        7: ('VII', 'LXX', 'DCC', ''),
        6: ('VI', 'LX', 'DC', ''),
        5: ('V', 'L', 'D', ''),
        4: ('IV', 'XL', 'CD', ''),
        3: ('III', 'XXX', 'CCC', 'MMM'),
        2: ('II',  'XX', 'CC', 'MM'),
        1: ('I', 'X', 'C', 'M'),
        0: ('', '', '', '')
    }

    @staticmethod
    def from_roman(roman_number):
        decimal_number = 0
        for i, c in enumerate(roman_number):
            current_number = RomanNumerals.roman_decimal_map[c]
            if i+1 < len(roman_number) and RomanNumerals.roman_decimal_map[c] < RomanNumerals.roman_decimal_map[roman_number[i+1]]:
                current_number *= -1
            decimal_number += current_number

        return decimal_number

    @staticmethod
    def to_roman(decimal_number):
        roman_number = ''
        for i, d in enumerate(str(decimal_number)):
            current_digit = (RomanNumerals.decimal_roman_map[int(d)])[len(str(decimal_number)) -i -1]
            roman_number += current_digit

        return roman_number

roman_helper = RomanNumerals()

print(roman_helper.from_roman('MCMXC'))

print(roman_helper.to_roman(1990))
