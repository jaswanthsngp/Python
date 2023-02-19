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
    def __init__(self, pname, age, cname, city, dealswith):
        super().__init__(cname, city, dealswith)
        self.pname= pname
        self.age= age
        print("Class Person")
    def personDetails(self):
        print(self.pname, self.age)

class Employee(Person):
    def __init__(self, pname, age, cname, city, dealswith, designation, salary):
        super().__init__(pname, age, cname, city, dealswith)
        self.designation= designation
        self. salary= salary
    def empDetails(self):
        print(self.pname, self.age)
        print(self.cname, self.city, self.dealswith)
        print(self.designation, self.salary)
        #Person.personDetails(self)
        #Company.compDetails(self)

x= Employee("John", 23, "Nanohard", "Mumbai", "Software", 'Manager', 50000)
x.empDetails()
