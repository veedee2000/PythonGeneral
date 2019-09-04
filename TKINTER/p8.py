from tkinter import *

root = Tk()

def functionOne():
    print("developers")
def functionTwo():
    print("testers")
def functionThree():
    print("Operations")
def functionFour():
    print("Rest Employees")
def functionOffice():
    print("officeLoacations")


menuOne = Menu(root)
root.config(menu = menuOne)

menudrop = Menu(menuOne)

menuOne.add_cascade(label = "EE divisions", menu = menudrop)
menudrop.add_command(label = "Developers", command = functionOne)
menudrop.add_command(label = "Testers", command = functionTwo)
menudrop.add_command(label = "Operations", command = functionThree)

menudrop.add_separator()
menudrop.add_command(label = "Rest Employees", command = functionFour)


menudropTwo = Menu(menuOne)
menuOne.add_cascade(label = "Office list", menu = menudropTwo)
menudropTwo.add_command(label = "IndiranagarOffice", command = functionOffice)
menudropTwo.add_command(label = "KeystoneOffice", command = functionOffice)
menudropTwo.add_command(label = "SpacesOffice", command = functionOffice)


root.mainloop()
 
