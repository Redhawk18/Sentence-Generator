# created 1/17/2022
# this file should create objects and append them into a longer string
from cmath import pi
from operator import truediv
import random
from pathlib import Path
from re import L
import sys
from words import *

def pickAndPrintRandomSentence(loopControl, randomSentence):
    wordlists = Path("wordlists")

    amountOfSentenceTypes = 1
    #it's easier to have the same random in two places because of the RandomSentence boolean
    rand = random.randrange(amountOfSentenceTypes)

    for i in range(0, loopControl):    
        if(randomSentence == True):
            rand = random.randrange(amountOfSentenceTypes)

        if rand == 0:
            #"The" adjective noun.
            n = noun(wordlists/"noun.txt")
            a = adjective(wordlists/"adjective.txt")
            print("The", a.randomizeWord(), n.randomizeWord() +".")
                
        else: 
            print("something is wrong...")


#user input
loopControl = 1 #these have to be passed to the function no matter what, even without input
randomSentence = True

loopBoolean = False
for arg in sys.argv:
    if(arg == "-help" or arg == "--help" or arg == "-h"):
        '''prints a list of commands with descriptions of their outputs'''
        print()
        print("-h or -help")
        print("\tprints a list of commands with descriptions of their outputs\n")
        print("-l or -loop")
        print("\ttakes value after and will loop input-th amount of times, will fail if input is below 0\n")
        print("-p or -phase")
        print("\tdisables the randomimze for sentence phases\n")

    elif(arg == "-l" or arg == arg == "-loop"):
        '''takes integer value after and will loop input-th amount of times, will fail if input is below 0'''
        loopBoolean = True

    elif(loopBoolean): 
        #messy code, but collects the value after the flag is called
        loopControl = int(arg)
        loopBoolean = False #so the value isn't overwritten

        #check loopControl for value integer
        if(loopControl < 1):
            print("Invalid loop input ")
            sys.exit()

    elif(arg == "-p" or arg == arg == "-phase"):
        '''disables the randomimze for sentence phases'''
        randomSentence = False


pickAndPrintRandomSentence(loopControl, randomSentence)