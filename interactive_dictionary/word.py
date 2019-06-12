'''
Class Word defines object Word
'''

class Word:

    def __init__(self, text = ""):
        self.text = text.lower()
        self.definitions = []
        self.similars = []
