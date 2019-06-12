#preguntamos que palabra quiere buscar
#buscamos la palabra en el diccionario
#si existe la mostramos por pantalla
#sino existe buscamos similares y le decimos al usuario que elija cual buscamos y mostramos la deinición por pantalla
#sino existen similares le decimos que canapé

from dictionary import Dictionary
from word import Word

dictionary = Dictionary("data.json")

word = Word(input("Please, enter a word: "))

if(dictionary.find(word)):
    print(word.definitions)

elif(dictionary.find_similars(word)):
    while True:
        selection = input(f"Sorry, but word '{word.text}' not appears in the dictionary. Maybe you're looking for '{word.similars[0]}'? Please enter Y or N ")

        if(selection.lower() == "y"):
            new_word = Word(word.similars[0])
            dictionary.find(new_word)
            print(new_word.definitions)
            break
        
        elif(selection.lower() == "n"):
            break

        else:
            print("You must select between Y or N")

else:
    print(f"Sorry, but word '{word.text}' is not in the dictionary")