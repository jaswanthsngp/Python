#Tuple

tuple1=()
print(tuple1)
tuple2=(1,2,3)
print(tuple2)
tuple2=(2,3,4)
print(tuple2)
tuple3=1,2
print(tuple3)
tuple4=("hello",)
tuple5=("hello")
print(type(tuple4))
print(type(tuple5))
tuple6=("hello", "world")
a,b=tuple6
print(a)
print(b)
a=(1,2,10,6,9)
print(a[::-1])          #prints tuple in reverse order
b=(10,20,30)
c=(40,50,60)
b,c=c,b                 #unpacks tuples b,c and puts values of c,b
print(b)
print(c)
print(len(b))
print(b.__sizeof__())

'''
#Tuples can have both homogenous and heterogenous data, but heterogenous is preferred
#tuples cannot be modified once created, but the exceptions are concatenations and re-initialisation
#lists in a tuple can be modified, without any problem
#can be initialised with or without brackets
#tuples can't hold single elment, if you want to, you have to put a comma and close the tuple
#tuples can be de-structured, and each element can be assigned to different variables
#tuples can be elements of lists too
'''
