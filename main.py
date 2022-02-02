# created 1/17/2022
# this file should create objects and append them into a longer string
import random
from words import *

amountOfSentenceTypes = 2
rand = random.randrange(amountOfSentenceTypes)

if rand == 0:
    #"The" adjective noun.
    n = noun("noun.txt")
    a = adjective("adjective.txt")
    print("The", a.print(), n.print() +".")

elif  rand == 1:
    #TODO logic
    print()
    
else: 
    print("amountOfSentenceTypes is wrong")
