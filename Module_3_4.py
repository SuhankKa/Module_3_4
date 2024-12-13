# Однокоренные

def single_root_words(root_word, *other_words):
    same_words=[]
    a = root_word.upper()
    
    for i in range(len(other_words)):
        b = other_words[i]
        c = str(b)
        d = c.upper()

        if a in d:
            same_words.append(b)
        if d in a:
            same_words.append(b)
        
    return same_words

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))   
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))    
print(single_root_words('Рост', 'РоСтоК', 'Подрос', 'перерост', 'подрастает'))   