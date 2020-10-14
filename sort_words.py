def sort_words(phrase):
    sorted_phrase = ""

    lst = phrase.split()
    lst.sort(key=lambda x: x.lower())

    return " ".join(lst)

#print(sort_words("string of words"))
#print(sort_words("banana ORANGE apple"))
