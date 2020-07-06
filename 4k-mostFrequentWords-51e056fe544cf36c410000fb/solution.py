import collections

def top_3_words(text):
    words_counter = collections.Counter()
    for word in text.split(' '):
        sanitized_word = word.lower().strip(' ,./;:\'_-[{]}()*&^%$#@!')
        if sanitized_word:
            words_counter[sanitized_word] = words_counter[sanitized_word] + 1

    return [k for k,v in words_counter.most_common(3)]

print(top_3_words('a a a  b  c c  d d d d  e e e e e'))

