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

toolbar = Frame(root, bg="aqua")
insertbutton = Button(toolbar, text="Insert files", command=function1)
insertbutton.pack(side=LEFT, padx=3, pady=2)

pbutton = Button(toolbar, text="Delete files", command=function1)
pbutton.pack(side=LEFT, padx=3, pady=2)

toolbar.pack(side=TOP, fill=X)

status = Label(root, text="This is status", bd = 1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM,fill = X)

root.mainloop()
