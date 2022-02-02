# created 1/17/2022
# this file should create objects and append them into a longer string
import random
from words import *

amountOfSentenceTypes = 1

if random.randrange(amountOfSentenceTypes) == 0:
    #sentence type 1
    #"The" adjective noun.
    
    n = noun("noun.txt")
    a = adjective("adjective.txt")
    print("The", n.print(), a.print() +".")
    
else: 
    print("amountOfSentenceTypes is wrong")
