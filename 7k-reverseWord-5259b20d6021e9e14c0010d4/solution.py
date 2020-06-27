def reverse_words(text):
    words = text.split(' ')
    reversed_words = [x[::-1] for x in words]
    return ' '.join(reversed_words)

def reverse_words_simplified(text):
    return ' '.join([x[::-1] for x in text.split(' ')])


assert reverse_words('eluwina ziomek kurde co jest') == reverse_words_simplified('eluwina ziomek kurde co jest')
print(reverse_words_simplified('eluwina ziomek kurde co jest'))