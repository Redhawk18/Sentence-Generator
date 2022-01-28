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

    def word(self):
        print("noun")
