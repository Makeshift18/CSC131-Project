########################################
# Name:
# Date:
# Description:
########################################
#import RPi.GPIO as GPIO
from Tkinter import *
from random import randint


Riddles = {1:"Riddle 1", 2:"Riddle 2" , 3:"Riddle 3" }
Used = []
Answers = ["Answer 1","Answer 2","Answer 3"]
answer = 0

def setGPIO():
    input1 = 17 #led 1
    input2 = 27  # 0
    input3 = 22 # reset
    input4 = 14 # send in an answer


# prints out a random riddle without chosing the same riddle over and over
# set answer to the coresponding riddle
# if you ask for more riddles than you have you get a print statement saying so
def randomRiddle():
    if len(Used) == len(Riddles):
        print "You have exaughsted the supply of riddles"
    else:   
        i = 0
        while i < 1:
            random = randint(1, len(Riddles))
            if random not in Used:
                i += 1        
        Used.append(random)        
        answer = Answers[random -1]
        print Riddles[random]
        print answer


#set up the button inputs and see if they are correct

randomRiddle()
randomRiddle()
randomRiddle()
randomRiddle() # dont have 4 riddles so prints out something special
print Used




