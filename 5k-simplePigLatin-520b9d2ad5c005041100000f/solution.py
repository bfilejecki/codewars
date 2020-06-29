import re

def pig_it(text):
    words = text.split(' ')
    pigged_words = []
    for word in words:
        rewriten_word = word
        stripped_word_match = re.match(r'\w+', word)
        if stripped_word_match is not None:
            stripped_word = word[stripped_word_match.start():stripped_word_match.end()]
            pigged_word =  stripped_word[0] + 'ay' if len(stripped_word) < 2 else stripped_word[1:] + stripped_word[0] + 'ay'
            rewriten_word = pigged_word
            
        pigged_words.append(rewriten_word)
    return ' '.join(pigged_words)

print(pig_it('Pig! latin, cool.'))
        
        
