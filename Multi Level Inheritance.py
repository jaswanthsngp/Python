#Multilevel Inheritance

class Company:
    def __init__(self, cname, city, dealswith):
        self.cname= cname
        self.city= city
        self.dealswith= dealswith
        print("Class Company")
    def compDetails(self):
        print(self.cname, self.city, self.dealswith)

class Person(Company):
    def __init__(self, pname, age, address, cname, city, dealswith):
        super().__init__(cname, city, dealswith)
        self.pname= pname
        self.age= age
        self.address= address
        print("Class Person")
    def personDetails(self):
        print(self.pname, self.age, self.address)

class Employee(Person):
    def __init__(self, pname, age, address, cname, city, dealswith, salary):
        super().__init__(pname, age, address, cname, city, dealswith)
        self. salary= salary
    def empDetails(self):
        print(self.pname, self.age, self.address)
        print(self.cname, self.city, self.dealswith)
        print(self.salary)
        #Person.personDetails(self)
        #Company.compDetails(self)

x= Employee("John", 23, "somewhere", "Nanohard", "Mumbai", "Software", 50000)
x.empDetails()
