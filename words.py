from abc import abstractclassmethod


class word():
    @abstractclassmethod
    def word(self):
        pass

class adjective(word):

    def word(self):
        print("adjective")

class verb(word):

    def word(self):
        print("verb")

class noun(word):
    #for subclasses of noun make it so you have word() and wordAndParent() which turns a random word from it's own list and it's parents
    def word(self):
        print("noun")
