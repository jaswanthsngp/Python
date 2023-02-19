#Multiple Inheritance
class Person:
    def __init__(self, pname, age, address, cname, city, dealswith):
        super().__init__(cname, city, dealswith)            #Now, the MRO comes into game
        self.pname= pname
        self.age= age
        self.address= address
        print("Class Person")
    def personDetails(self):
        print(self.pname, self.age, self.address)

class Company:
    def __init__(self, cname, city, dealswith):
        super().__init__()
        self.cname= cname
        self.city= city
        self.dealswith= dealswith
        print("Class Company")
    def compDetails(self):
        print(self.cname, self.city, self.dealswith)

class Employee(Person, Company):
    def __init__(self, pname, age, address, cname, city, dealswith, salary):
        #Person.__init__(self, pname, age, address)
        #Company.__init__(self, cname, city, dealswith)
        super().__init__(pname, age, address,cname, city, dealswith)        #super() refers only to 
        #super().__init__(cname, city, dealswith)                           #the first parent class
        self. salary= salary
    def empDetails(self):
        print(self.pname, self.age, self.address)
        print(self.cname, self.city, self.dealswith)
        print(self.salary)
        #Person.personDetails(self)
        #Company.compDetails(self)

x= Employee("John", 23, "somewhere", "Nanohard", "Mumbai", "Software", 50000)
x.empDetails()

#Method Resolution Order (MRO):                                                            Object Class
'''                                                                                         /      \     
    Searches for the constructor in current class first                                    A        B   
    On encounter with super(), it searches in parent class                                  \      /
    On encounter with super() in super base class, it searches in 'Object Class',               C
    which is parent of every other class, for next parent and keeps moving to next,
    until all the parents are done.
'''
