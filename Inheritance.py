class Person:
    def __init__(self, fname, lname):
        self.fname= fname
        self.lname= lname
    def printname(self):
        print(self.fname, self.lname)

class Student(Person):                              #Parent class is denoted with child during declaration
    def __init__(self, fname, lname, year):
        #Person.__init__(self, fname, lname)        #Parent class' __init__() shall be called to access parent's methods
        super().__init__(fname, lname)              #or simply call super().__init__() which automatically calls parent
        self.graduationyear= year
    def childfn(self):
        print("Congrats", self.fname, self.lname,"in passing out in", self.graduationyear)

class Studies(Student):                             
    def __init__(self, fname, lname, year, course):
        super().__init__(fname, lname, year)        #super() refers to only parent which is one-level up
        self.course= course
    def grndchld(self):
        print(self.fname, self.lname, self.graduationyear, self.course)

y= Studies("John", "Doe", 2020, "Tech")
y.printname()
y.childfn()
y.grndchld()
