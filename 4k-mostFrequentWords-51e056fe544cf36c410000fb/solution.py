### IT DOESN"T WORK

import collections
import re

def top_3_words(text):
    word_regex = re.compile(r'^[\'A-Za-z]+$')
    words_counter = collections.Counter()
    for word in text.split(' '):
        lower_word = word.lower()
        sanitized_word = lower_word.strip(',.!@#$%^&*()-={[]}:;\\/<>~`\'')

        if sanitized_word and word_regex.fullmatch(sanitized_word):
            words_counter[sanitized_word] = words_counter[sanitized_word] + 1

    return [k for k,v in words_counter.most_common(3)]

print(top_3_words('a a a  b  c c  d d d d  e e e e e'))

