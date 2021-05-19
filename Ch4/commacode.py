
def commacode(words):
    new_words = ''
    if words == []:
        return ''
    for index, word in enumerate(words):
        if index != len(words)-1:
            new_words += word + ', '
        else:
            new_words +='and ' + word  
    return new_words

words=['spam', 'eggs', 'bacon', 'marijuana']
empty_words = []
print (commacode(words))
print (commacode(empty_words))
