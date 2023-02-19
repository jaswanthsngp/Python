#GUI
#built in module tkinter
#tkinter can be expanded as toolkit interface
from tkinter import *

def hello():
    print('Hello Python')
    #This function gets excecuted when button is pressed

root= Tk()                  #Declaring an object of class Tk()
root.geometry('300x350')    #defines initial size of the window
root.maxsize(900, 600)
root.minsize(200, 300)
root.title('GUI Window')    #Adds a title to the window
mylabel= Label(text= "This is a python GUI Lecture", fg= 'yellow', bg= 'red', font='calibri 19 bold', relief= RAISED, borderwidth= 5)
#Label is a class which can be inserted into interface, so we create an object of it
mylabel.pack(side= LEFT, anchor= 's')              #pack inserts the label into window
#side and achor tells about the alignment, one in left, right, etc and other in north, south, etc.
photo= PhotoImage(file= 'JS.png') #making a photo as an object
photolabel= Label(image= photo, relief= SOLID, borderwidth= 5, padx= 20, pady=23)       #relief= SUNKEN/RAISED/RIDGE/FLAT/GROOVE/SOLID #style of border
photolabel.pack()
f= Frame(root, borderwidth= 2, bg= 'grey', relief= FLAT)
f.pack(side= LEFT)
b= Button(f, fg= 'blue', text= 'print', bg='yellow', command= hello)
b.pack()
#b.bind('<Button-1>', hello) can also be used instead of command, but hello should have a self parameter
root.mainloop()
#mainloop is the last statement of GUI, which makes it run
