# created 1/17/2022
# this file should create objects and append them into a longer string
import random
from pathlib import Path

from words import *

wordlists = Path("wordlists")

amountOfSentenceTypes = 1
rand = random.randrange(amountOfSentenceTypes)

if rand == 0:
    #"The" adjective noun.
    n = noun(wordlists/"noun.txt")
    a = adjective(wordlists/"adjective.txt")
    print("The", a.randomize_word(), n.randomize_word() +".")
    
else: 
    print("amountOfSentenceTypes is wrong")
