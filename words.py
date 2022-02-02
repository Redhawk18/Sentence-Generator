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

    def print(self):
        '''this function returns a random word from the list passed into the object'''
        return random.choice(self.wordlist)

    def printSelfAndParents(self, wordlist):
        '''makes a new list that has the strings from the wordlist and the object parent's wordlist and returns one of them'''
        wordListWithParents = ()
        
        for i in wordlist: #current object's list
            line = wordlist[i]
            wordListWithParents.append(line)
        
        for j in super.wordlist: #parent's list
            line = super.wordlist[j]
            wordListWithParents.append(line)

        #both lists are in the same new list now, and there's no need to sort
        return random.choice(self.wordListWithParents)

class adjective(word):
    pass

class verb(word):
    pass

class noun(word):
    pass
