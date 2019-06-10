import json
import difflib

with open("data.json") as f:
    data = json.load(f)

def translate(w):
    if(w in data):
       return data[w]

    elif(len(alternatives(w)) > 0):
        while True:
            confirmation = input(f"Sorry, but word '{w}' is not in the dictionary.\nMaybe you look for: {alternatives(w)} ? (please enter Y or N) ")
        
            if(confirmation.lower() == "y"):
                return data[alternatives(w)]

            elif(confirmation.lower() == "n"):
                break

            else:
                print("Sorry but you must answer Y or N")

    else:
        return f"Sorry, but word '{w}' is not in the dictionary. Please double check it"

def alternatives(w):
    return difflib.get_close_matches(w, data.keys())[0]

word = input("Please enter a word: ")
translation = translate(word.lower())

if(type(translation) == list):
    for item in translation:
        print(item)
else:
    print(translation)