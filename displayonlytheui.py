from Tkinter import *

class Game(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)


    def setupGUI(self):
        l1 = Label(self.master, text = "Riddle", bg = "lightgrey", width = 100, height = 10)
        l1.grid(row = 0, column = 0, columnspan = 5, rowspan = 2, sticky=N+S+E+W)


        ## abcd for every fake answer
        l2 = Label(self.master, text ="A)", bg = "red", width = 5, height = 5)
        l2.grid(row = 4, column = 0, rowspan = 2,  sticky = W)
        l3 = Label(self.master, text ="B)", bg = "blue", width = 5, height = 5)
        l3.grid(row = 4, column = 3, rowspan = 2, sticky = W)
        l4 = Label(self.master, text ="C)", bg = "yellow", width = 5, height = 5)
        l4.grid(row = 6, column = 0, rowspan = 2, sticky = W)
        l5 = Label(self.master, text ="D)", bg = "green",width = 5, height = 5)
        l5.grid(row = 6, column = 3, rowspan = 2, sticky = W)



window = Tk()
g = Game(window)
g.setupGUI()
window.mainloop()       
