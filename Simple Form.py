from tkinter import *

def submit():
    s= f'{fname.get()} {lname.get()} {sec.get()} {roll.get()} {group.get()}\n'
    #get method is used to fetch the values from form
    f= open('StudentData.txt', 'a')
    f.write(s)
    f.close()
    print(s)

root= Tk()
root.geometry('300x300')
root.maxsize(1800, 1200)
root.minsize(300, 200)
root.title('Simple Form')

#Naming Labels
fnamel= Label(root, text='First Name')
lnamel= Label(root, text='Last Name')
secl= Label(root, text= 'Section')
rolll= Label(root, text= 'Roll Number')
groupl= Label(root, text= 'Group')

#Declaring form variables
fname= StringVar()
lname= StringVar()
sec= StringVar()
roll= StringVar()
group= IntVar()


#Form input elements
fnamee= Entry(root, textvariable= fname)
lnamee= Entry(root, textvariable= lname)
sece= Entry(root, textvariable= sec)
rolle= Entry(root, textvariable= roll)
groupf= Frame(root)
group1e= Radiobutton(groupf, text= 'G1', variable= group, value= 1)
group2e= Radiobutton(groupf, text= 'G2', variable= group, value= 2)
submite= Button(text= 'Submit', command= submit)


#Inserting objects into window, using grid layout to place them
fnamel.grid(row=0, column= 0)
fnamee.grid(row=0, column= 1)
lnamel.grid(row=1, column= 0)
lnamee.grid(row=1, column= 1)
secl.grid(row=2, column= 0)
sece.grid(row=2, column= 1)
rolll.grid(row=3, column=0)
rolle.grid(row=3, column=1)
groupl.grid(row=4, column=0)
groupf.grid(row= 4, column= 1)
group1e.grid(row=0, column= 0)
group2e.grid(row=0, column= 1)
submite.grid(row=5, column=1)

root.mainloop()
