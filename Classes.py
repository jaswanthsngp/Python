#Classes

class Computer:                                 #Classes are created using 'class' keyword, and generally named in Title case
    def __init__(this, c, r):                   #Data of classes is initialised by __init__() method, which acts as a constructor
        this.cpu= c
        this.ram= r
    def config(this):                           # 'self' represents that data belongs to this object, anyother word can also be used
        print("Configuration is ", this.cpu, this.ram)

com1= Computer('i5', 16)                        #Objects are declared this way
com2= Computer('i7', 8)

#Computer.config()                              #Raises error as self is a required argument. Works if fn is declared without self
Computer.config(com1)                           #Functions are called this way
com2.config()                                   #This way too
print(com2.__sizeof__())                        #size of class depends on datatypes and methods used
#memory is allocated to class in heap

#Class variables can be accessed publicly too
print(com2.cpu)

#Class variables and objects can be deleted using 'del' keyword
#del com2.ram
#print(com1.ram)
#print(com2.ram)
#del com2
#print(com2)
