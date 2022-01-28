# created 1/17/2022
# this file should create objects and append them into a longer string
import random

fileOutput = []
#file = open("adjective.txt", "r")
for i in open("adjective.txt", "r"):
    line = i.strip()
    #print(i.strip())
    fileOutput.append(line)
    
    #print(line)
#test commit desktop
print(random.choice(fileOutput))