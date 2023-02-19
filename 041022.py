class Department:
    def __init__(self):
        pass
    def get(self, dId, dName):
        self.dId= dId
        self.dName= dName

class Faculty(Department):
    def __init__(self):
        super().__init__()
    def get(self, fId, fName, course, dId, dName):
        super().get(dId, dName)
        self.fId= fId
        self.fName= fName
        self.course= course
    def display(self):
        print(self.fId, self.fName, self.course, self.dId, self.dName)

class Student(Department):
    def __init__(self):
        super().__init__()
    def get(self, regNo, sName, pName, dId, dName):
        super().get(dId, dName)
        self.regNo= regNo
        self.sName= sName
        self.pName= pName
    def display(self):
        print(self.regNo, self.sName, self.pName, self.dId, self.dName)

fac= Faculty()
fac.get(7, 'Dr. Someone', 'Python', 3, 'SCSE')
fac.display()

st= Student()
st.get(121, 'Anyone', 'CSE', 3, 'SCSE')
st.display()
