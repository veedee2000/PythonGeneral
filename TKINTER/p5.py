from tkinter import *

root = Tk()

def function():
    print("RISOTTO NIGGA U CLICKED THE BUTTON")

label1 = Button(root, text="Click Here", command=function)
label1.pack()

root.mainloop()
