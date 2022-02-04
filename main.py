# created 1/17/2022
# this file should create objects and append them into a longer string
from cmath import pi
import random
from pathlib import Path
import sys
from words import *

def pickRandomSentence():
    wordlists = Path("wordlists")

    amountOfSentenceTypes = 1
    rand = random.randrange(amountOfSentenceTypes)

    if rand == 0:
        #"The" adjective noun.
        n = noun(wordlists/"noun.txt")
        a = adjective(wordlists/"adjective.txt")
        print("The", a.randomizeWord(), n.randomizeWord() +".")
        
    else: 
        print("amountOfSentenceTypes is wrong")


#user input
for arg in sys.argv:
    print(arg)

