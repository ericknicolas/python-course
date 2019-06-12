'''
Class Dictionary defines object Dictionary
'''
import json
from word import Word
from difflib import get_close_matches

class Dictionary:

    def __init__(self, database):
        with open(database) as f:
            self.data = json.load(f)
    
    def __str__(self):
        return str(self.data)
    
    def find(self, w):
        if(w.text in self.data):
            w.definitions = self.data[w.text]
            return True
        else:
            return False

    def find_similars(self, w):
        w.similars = get_close_matches(w.text, self.data.keys())
        
        return (len(w.similars) > 0)
        