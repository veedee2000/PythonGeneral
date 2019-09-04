from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()
newline = canvas.create_line(100,100,4,1)
o = canvas.create_line(0,-0,10,10,fill = "purple")

root.mainloop()
