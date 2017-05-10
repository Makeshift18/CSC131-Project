from Tkinter import *
from random import randint
import RPi.GPIO as GPIO
import time

class Game(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)


    def setupGUI(self):
        l1 = Label(self.master, text = "Riddle", bg = "lightgrey", width = 100, height = 10)
        l1.grid(row = 0, column = 0, columnspan = 3, rowspan = 2, sticky=N+S+E+W)
        l2 = Label(self.master, text ="A)", bg = "red", width = 5, height = 5)
        l2.grid(row = 3, column = 0, sticky = W)
        l3 = Label(self.master, text ="B)", bg = "blue", width = 5, height = 5)
        l3.grid(row = 3, column = 2, sticky = W)
        l4 = Label(self.master, text ="C)", bg = "yellow", width = 5, height = 5)
        l4.grid(row = 4, column = 0, sticky = W)
        l5 = Label(self.master, text ="D)", bg = "green",width = 5, height = 5)
        l5.grid(row = 4, column = 2, sticky = W)





    def setupGPIO():
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        Input_1 = GPIO.input(17)
        Input_2 = GPIO.input(27)
        Input_3 = GPIO.input(22)
        Input_4 = GPIO.input(5)
        
        







window = Tk()
g = Game(window)
g.setupGUI()
window.mainloop()
