import RPi.GPIO as GPIO
from Tkinter import *
from random import randint
import time

class Game(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # these variable are updated throught the program
        self.Riddle = StringVar()
        self.time = StringVar()
        self.playerans = StringVar()

        # these set the variables to the defaults and each has its own function for when the variable changes
        self.playerans.set("Current Answer = {}".format(playerAnswer))  
        self.time.set("Time Remaining = {}s".format(sec))
        self.Riddle.set(answer.values()[a])





    def setupGPIO(self):
        # set up all the GPIO inputs
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        Input_1 = GPIO.input(17)
        Input_2 = GPIO.input(27)
        Input_3 = GPIO.input(22)
        Input_4 = GPIO.input(5)


    # a start button for the game
    # press start starts the game
    def startup(self):
        start = Button(self.master, text="Press to Start", command=self.setupGUI)
        start.pack()
        

    def setupGUI(self):
        # this displays the riddle at the top
        l1 = Label(self.master, textvariable = self.Riddle, bg = "lightgrey", width = 122, height = HEIGHT * 2, wraplength = 300)
        l1.grid(row = 0, column = 0, columnspan = 5, rowspan = 2)
        
        ## abcd for every fake answer
        # meant to confuse
        l2 = Label(self.master, text ="A)", bg = "lightgrey", width = WIDTH/6, height = HEIGHT)
        l2.grid(row = 4, column = 0, rowspan = 2)
        
        l3 = Label(self.master, text ="B)", bg = "lightgrey", width = WIDTH/6, height = HEIGHT)
        l3.grid(row = 4, column = 3, rowspan = 2)
        
        l4 = Label(self.master, text ="C)", bg = "lightgrey", width = WIDTH/6, height = HEIGHT)
        l4.grid(row = 6, column = 0, rowspan = 2)
        
        l5 = Label(self.master, text ="D)", bg = "lightgrey",width = WIDTH/6, height = HEIGHT)
        l5.grid(row = 6, column = 3, rowspan = 2)


        # these are the "asnwers" could all be buttons
        # i would of liked to been able to change them
        # mainly ment to confuse
        l7 = Label(self.master, text ="Sponge", bg = "lightgrey",width = WIDTH /3, height = HEIGHT)
        l7.grid(row = 4, column = 1, columnspan = 1,)
        
        l8 = Label(self.master, text ="Sponge2", bg = "lightgrey",width = WIDTH /3, height = HEIGHT)
        l8.grid(row = 4, column = 4, columnspan = 1)

        l9 = Label(self.master, text ="Sponge3", bg = "lightgrey",width = WIDTH /3, height = HEIGHT)
        l9.grid(row = 6, column = 1, columnspan = 1,)

        l10 = Label(self.master, text ="Sponge4", bg = "lightgrey",width = WIDTH /3, height = HEIGHT)
        l10.grid(row = 6, column = 4, columnspan = 1,)


        # the player answer is displayed here at the bottom
        playerinput = Label(self.master, textvariable = self.playerans, bg = "grey", width = 122, height = HEIGHT /2)
        playerinput.grid(row = 8,columnspan = 5)


        # adds a timer

        l6 = Label(self.master, textvariable = self.time, bg = "red", width = WIDTH/6)
        l6.grid(row = 0, column = 4, sticky = N+E)
        self.update_clock(sec)


    # controlls the timer if the time runs out the game ends
    def update_clock(self,sec):
        if sec >= 0:
            self.time.set("Time Remaining = {}s".format(sec))
            g.after(1000, self.update_clock, sec - 1)
                            
        else:
            self.endgame(0)

    # udates the player input whenever a button is pressed
    def update_input(self):
        self.playerinput.set("Current Answer = {}".format(playerAnswer))

        
    # when the timer hits 0 or you submit an answer and get it right or not
    def endgame(self, winconditon):
        if winconditon == 1:
            self.Riddle.set = "Congratulations you win!"
            
        else:
            self.Riddle.set("Congratulations you lose!")


    def combineAnswer(playerAnswer):            # This subroutine condenses the playerAnswer list
                                                # into a string.
        playerAnswer = ''.join(map(str, playerAnswer))
        return playerAnswer

    def compareAnswers(playerAnswer, answer):   # This subroutine compares the answer provided by 
        if playerAnswer == answer.keys()[a]:    # the player to the answer in the key of the Riddle
            #print "That is correct"            # dictionary.
            self.engame(1)
        else:
            #print "That is not correct"
            self.endgame(0)

    def submit(playerAnswer):
        playerAnswer = self.combineAnswer(playerAnswer)
        #print "The correct answer is {}".format(answer.keys()[a])
        #print "Your answer is {}".format(playerAnswer)
        self.compareAnswers(playerAnswer,answer)



    def play(self):
        try:
            while True:

                # Takes the inputs and then do something
                
                if Input_1 == False:
                    self.playerAnswer.append("1")       # add 1 to player answer
                    self.combineAnswer
                    self.unpdate_input()
                    time.sleep(0.5)
                elif Input_2 == False:
                    self.playerAnswer.append("0")
                    self.combineAnswer
                    self.unpdate_input()
                    time.sleep(0.5)
                elif Input_3 == False:
                    self.playerAnswer = []
                    #print "your answer has been reset"
                    self.unpdate_input()
                    time.sleep(0.5)
                elif Input_4 == False:
                    submit(self.playerAnswer)
                    time.sleep(0.5)
                else:
                    time.sleep(0.2)
        except KeyboardInterrupt:
            #Ctrl + C resets the GPIO pins
            GPIO.cleanup()
        
        
################################################################################################    
sec =  120                                  # number of seconds on the timer
playerAnswer = []                           # This variable is the player's input.
answer = {"111111111010001010101":"1 have a new fr1end. \
The new fr1end plays a new game. \
The new game 1s a l1ttle tr1ck1ng. \
The tr1ck 1s t0 f1nd the 0ne that's 0ut 0f place.\
W1th zer0 be1ng the 0bv10us ba1t.","100101001100101110100":"1 c0mplement the tw0 that have ne1ther been 0ne. \
1 c0mplement the 0ne that w1ll never s1ng f0r y0u. \
1 c0mplement my style of r1ddle mak1ng w1th a clue. \
The answer cannot be the secret talk1ng t0 y0u.","100100111010101011010":"1 L00k and see r1ddles that d0 n0t make any sense. \
The l1nes they rhyme., 1t passes t1me, but the c0ntext 1s s0 dense. \
1 d0n't understand the numbered band w1th le0pard hand. \
But 1 st1LL w0nder what 1t c0uld have meant."}
a = randint(0,2)                            # This Variable is a placeholder for the number
                                            # that will represent which item in the dictionary
                                            # is selected. It can be 2, 1, or 0 right now.



WIDTH = 120
HEIGHT = 5
window = Tk()
window.title("R1ddles 0f Myster1a")
g = Game(window)
g.setupGPIO()
g.startup()
g.play()
window.mainloop()

