def pig_latin(word):
    if word[0] in "aeiou":
        return word + "ay"
    else:
        return word[1:] + word[0] + "ay"

word = input("introduce a word to be coded... \n")
print(pig_latin(word))