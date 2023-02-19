#Polymorphism
    #Operator Overlading
        #Same operators used for different purposes
    #Method Overloading/ Function Overloading
        #Same named functions with different arguments
        #Not supported in Python, except in built-in ways
        #Instead, default arguments are used.
    #Method Overriding
        #Same functions defined in parent and child class
        #Child functions get excecuted, overriding parent methods
    #Duck Typing


#Method Overloading
class A:
    def sum(self, a):
        print("First sum method", a)

    def sum(self):
        print("Second sum method")      #Takes this as redifinition, not overloading
obj= A()
obj.sum()
#obj.sum(12)


#Method Overriding
class Add:
    def result(self, a, b):
        print("Addition", a+b)          #Parent class method

class Multi(Add):
    def result(self, a, b):
        super().result(a, b)
        print("Multiplication", a*b)    #Child class method, overrides parent method

m= Multi()
m.result(10,20)
