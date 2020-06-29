def first_non_repeating_letter(string):
    for s in string:
        count = string.upper().count(s.upper()) if s.isalpha() else string.count(s)
        if count == 1:
            return s
    return ''

print(first_non_repeating_letter('stress'))
print(first_non_repeating_letter('moonmen'))
print(first_non_repeating_letter('~><#~><'))
print(first_non_repeating_letter('sTreSS'))