from abc import abstractclassmethod
from fileinput import close
import random

def readTextfile(filename):
    '''Takes a file name and creates a list and output's file content to list in all lowercase'''
    fileOutput = []
    for i in open(filename, "r"):
        line = i.strip().lower()
        fileOutput.append(line)
    close()
    return fileOutput

class word():
    @abstractclassmethod

    def __init__(self, fileName):
        self.wordlist = readTextfile(fileName)

    def __len__(self):
        return len(self.wordlist)

    def randomize_word(self):
        '''this function returns a random word from the list passed into the object'''
        return random.choice(self.wordlist)

class adjective(word):
    pass

class verb(word):
    pass

class noun(word):
    pass
