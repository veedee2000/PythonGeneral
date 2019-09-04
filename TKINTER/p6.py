from tkinter import *

class mybuttons:

    def __init__(self,rootone):
        frame = Frame(rootone)
        frame.pack()

        self.printbutton = Button(frame, text="Click Here", command=self.printmessage)
        self.printbutton.pack(fill=Y)

        self.quitbutton = Button(frame, text="Exit", command=frame.quit)
        self.quitbutton.pack(side=LEFT, fill=X)

    def printmessage(self):
        print("BUTTON CLICKED")

root = Tk()
b = mybuttons(root)

root.mainloop()
