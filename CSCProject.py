########################################
# Name:
# Date:
# Description:
########################################
#import RPi.GPIO as GPIO
from Tkinter import *
from random import randint
from time import time

def setGPIO():
    input1 = 17 #led 1
    input0 = 27  # 0
    reset = 22 # reset
    answer = 13 # send in an answer
    GPIO.setup(input1, GPIO.IN, GPIO.PUD_DOWN)
    GPIO.setup(input0, GPIO.IN, GPIO.PUD_DOWN)
    GPIO.setup(reset, GPIO.IN, GPIO.PUD_DOWN)
    GPIO.setup(answer, GPIO.IN, GPIO.PUD_DOWN)

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


def checkanswer():
    while len(playeranswer) > 1:
        playeranwser(0) + playeranwser(1)

    if playeranwser == answer
        
def caclscore():
    pass

Riddles = {1:"Riddle 1", 2:"Riddle 2" , 3:"Riddle 3" }
Used = []
Answers = ["Answer 1","Answer 2","Answer 3"]
answer = 0
playeranswer = []
#set up the button inputs and see if they are correct

randomRiddle()
randomRiddle()
randomRiddle()
randomRiddle() # dont have 4 riddles so prints out something special
print Used
#setGPIO()


# actual part of the code
# still needs to be put in a gui
try:
    while(True):
        #start a timer
        start = time()
        randomRiddle()
        if input1:
            playeranswer.append("1")

        if input0:
            playeranswer.append("0")

        if reset:
            playeranswer = []
            
        if answer:
            checkanswer()
            
except KeyboardInterrupt:
    # reset the GPIO pins
    GPIO.cleanup()
