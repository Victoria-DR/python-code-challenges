def palindrome(phrase):
    phrase = phrase.lower()

    character = 0
    while character < len(phrase):
        if phrase[character].isalpha():
            character += 1
        else:
            phrase = phrase.replace(phrase[character], "")
        
    return phrase == phrase[::-1]

#print(palindrome("race car"))
#print(palindrome("Go hang a salami - I'm a lasagna."))
