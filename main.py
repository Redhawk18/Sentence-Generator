# created 1/17/2022
# this file should create objects and append them into a longer string
from fileinput import close
import random
from words import *

def readTextfile(filename):
    fileOutput = []
    for i in open(filename, "r"):
        line = i.strip().lower()
        fileOutput.append(line)
    close()
    return fileOutput

#most basic sentence
#test change


#TODO make objects to make the words more print statements readable and to learn about python classes
#TODO add some kind of random so different sentences
maxAmountOfSentenceType = 2

if random.randrange(maxAmountOfSentenceType) == 0:
    #sentence type 1
    #The adjective noun.
    n = noun(readTextfile("adjective.txt"))
    #print("The", random.choice(readTextfile("adjective.txt")), random.choice(readTextfile("noun.txt")) +".")
    print(n)
else: 
    print("no")
