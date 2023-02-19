from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from time import *
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pwd4DBM$",
    database="alltables"
    )
############################################### LOGIC AND DATABASE HANDLING ###############################################################

mycursor= mydb.cursor()

#Schemas taken for DataBase
#car(regNo varchar(10) primary key, chasisNo varchar(17), manufacturer varchar(20), model varchar(30), seats int)
#person(name varchar(30), age int, gender varchar(6), licence varchar(20) primary key, contact int, emergencyContact int);
#rent(carNo varchar(10), plicence varchar(20), tookAt int)


def book():
    #This function handles all the inputs taken to book a car
    print(f'{name.get()} {int(age.get())} {gender.get()} {licence.get()} {mobile.get()} {emergencyMobile.get()} {car.get()}')
    ################# Collecting Variables #############################
    personValues= (name.get(), age.get(), gender.get(), licence.get(), mobile.get(), emergencyMobile.get())
    carValues= car.get().split()
    rentValues= (carValues[0], personValues[3], int(time()))

    ################ Updating DataBases ##############################
    ########## Checking if the car is already booked ##############
    mycursor.execute('select carNo from rent;')
    bookedCars= mycursor.fetchall()
    if (carValues[0], ) in bookedCars:
        tkinter.messagebox.showerror('Sorry', 'The car is already booked. Please select another')
    else:
    	########### Updating PERSON Table ###############
        mycursor.execute("select licence from person;")
        person= mycursor.fetchall()
        print(person)
        ### Checking if the person details are already in DB ###
        if (personValues[3], ) in person:
            #### Taking input from user to update details or not ####
            if tkinter.messagebox.askyesno('Update?', 'A database already exists with this licence. Overwrite it?'):
                mycursor.execute('delete from person where licence= %s', (personValues[3], ))
                mycursor.execute("insert into person values(%s, %s, %s, %s, %s, %s)", personValues)
                mydb.commit()
        else:
            mycursor.execute("insert into person values(%s, %s, %s, %s, %s, %s)", personValues)
            mydb.commit()
        ############ Updating RENT Table ################
        mycursor.execute("insert into rent values(%s, %s, %s)", rentValues)
        mydb.commit()
        tkinter.messagebox.showinfo('Success', 'Your car is booked')
    
####### Fetching Car and Person details from DB to display in tkinter.ttk.Combobox ##########
mycursor.execute("select regno, model, seats from car where regno not in (select carNo from rent)")
cars= mycursor.fetchall()
mycursor.execute("select carNo from rent;")
rCars= mycursor.fetchall()
mycursor.execute("select plicence from rent;")
rLicences= mycursor.fetchall()
print(cars)

def relieve():
    #This function handles Billing and removal of car
    print(f'{rCar.get()} {rLicence.get()}')
    mycursor.execute("select plicence, tookAt from rent where carNo= %s", (rCar.get(), ))
    v= mycursor.fetchall()
    ### Validation and Billing ###
    if v[0][0]==rLicence.get():
        print(int(time())- v[0][1])
        tkinter.messagebox.showinfo('Bill', f'The rent you have to pay is {1*(int(time())- v[0][1])//60} Rupees')
        ### Removal of rent details from DB ###
        mycursor.execute("delete from rent where carNo= %s", (rCar.get(), ))
        mydb.commit()
    else:
        tkinter.messagebox.showwarning('Wrong Details', 'Please select a valid car-licence combination')
    
##################################################### GUI Part #################################################################
#initial framing
root= Tk()
root.geometry('350x350')
root.maxsize(1800, 1200)
root.minsize(350, 350)
root.title('Car Booking System')

#Declaring frames that to put elements
takeCar= Frame(root, borderwidth= 1, relief= SOLID, padx= 5, pady= 5)
takeCar.pack()
blankLine= Label(root, text= ' ')
blankLine.pack()
relieveCar= Frame(root, borderwidth= 1, relief= SOLID, padx= 5, pady= 5)
relieveCar.pack()

#Declaring all the labels
#Labels to book car
takeCarLabel= Label(takeCar, text='Book Car', font= 'Calibri 14 bold italic')
nameLabel= Label(takeCar, text= 'Name')
ageLabel= Label(takeCar, text= 'Age')
genderLabel= Label(takeCar, text= 'Gender')
licenceLabel= Label(takeCar, text= 'Driving Licence Number')
mobileLabel= Label(takeCar, text= 'Mobile Number')
emergencyMobileLabel= Label(takeCar, text= 'Emergency Moblie')
carLabel= Label(takeCar, text= 'Select the car')
#Labels to relieve car
relieveLabel= Label(relieveCar, text='Relieve Car', font= 'Calibri 14 bold italic')
rCarLabel= Label(relieveCar, text= 'Select the Car')
rLicenceLabel= Label(relieveCar, text= 'Select the Licence')


#Declaring all the input variables
#to book
name= StringVar()
age= IntVar()
gender= StringVar()
licence= StringVar()
mobile= IntVar()
emergencyMobile= IntVar()
car= StringVar()
#to relieve
rCar= StringVar()
rLicence= StringVar()


#Declaring all the input elements
#to book
nameEntry= Entry(takeCar, textvariable= name)
ageEntry= Spinbox(takeCar, from_= 18, to= 100, textvariable= age)
genderFrame= Frame(takeCar)
genderMale= Radiobutton(genderFrame, text= 'Male', variable= gender, value= 'Male')
genderFemale= Radiobutton(genderFrame, text= 'Female', variable= gender, value= 'Female')
genderOther= Radiobutton(genderFrame, text= 'Other', variable= gender, value= 'Other')
licenceEntry= Entry(takeCar, textvariable= licence)
mobileEntry= Entry(takeCar, textvariable= mobile)
emergencyMobileEntry= Entry(takeCar, textvariable= emergencyMobile)
carEntry= ttk.Combobox(takeCar, textvariable= car)
submitEntry= Button(takeCar, text= 'Book', command= book)
#to relieve
rLicenceEntry= ttk.Combobox(relieveCar, textvariable= rLicence)
rCarEntry= ttk.Combobox(relieveCar, textvariable= rCar)
relieveEntry= Button(relieveCar, text= 'Relieve', command= relieve)
#defining Spinboxes and Comboboxes
carEntry['values']= cars
carEntry['state']= 'readonly'
ageEntry['state']= 'readonly'
rLicenceEntry['values']= rLicences
rLicenceEntry['state']= 'readonly'
rCarEntry['values']= rCars
rCarEntry['state']= 'readonly'

#placing inputs according to grids
takeCarLabel.grid(row= 0, column= 0)
nameLabel.grid(row= 1, column= 0)
nameEntry.grid(row= 1, column= 1)
ageLabel.grid(row= 2, column= 0)
ageEntry.grid(row= 2, column= 1)
genderLabel.grid(row= 3, column= 0)
genderFrame.grid(row= 3, column= 1)
licenceLabel.grid(row= 4, column= 0)
licenceEntry.grid(row= 4, column= 1)
mobileLabel.grid(row= 5, column= 0)
mobileEntry.grid(row= 5, column= 1)
emergencyMobileLabel.grid(row= 6, column= 0)
emergencyMobileEntry.grid(row= 6, column= 1)
carLabel.grid(row= 7, column= 0)
carEntry.grid(row= 7, column= 1)
submitEntry.grid(row= 8, column= 1)
#placing radiobuttons inside frame
genderMale.grid(row= 0, column= 0)
genderFemale.grid(row= 0, column= 1)
genderOther.grid(row= 0, column= 2)
#form elements to relieve car
relieveLabel.grid(row= 0, column= 0)
rCarLabel.grid(row= 1, column= 0)
rCarEntry.grid(row= 1, column= 1)
rLicenceLabel.grid(row= 2, column= 0)
rLicenceEntry.grid(row= 2, column= 1)
relieveEntry.grid(row= 3, column= 1)

takeCar.mainloop()
