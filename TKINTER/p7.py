from tkinter import *

def function1():
    print("HELLO THE GODFATHER")

root = Tk()

mymenu = Menu(root)
root.config(menu=mymenu)

submenu = Menu(mymenu)

mymenu.add_cascade(label="File", menu=submenu)

submenu.add_command(label="Save", command=function1)
submenu.add_command(label="Delete", command=function1)
submenu.add_separator()
submenu.add_command(label="Change", command=function1)

newmenu = Menu(mymenu)
mymenu.add_cascade(label="Edit", menu=newmenu)
newmenu.add_command(label="LOL BITCH", command=function1)


root.mainloop()
