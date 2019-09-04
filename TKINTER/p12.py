from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("TITLE","THIS IS COOL BRUH")
response = tkinter.messagebox.askquestion("Question1","want it?")
if response == "yes":
    print("take it")

root.mainloop()
