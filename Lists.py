#List

student_name= ["Shaun", "Linh", "Ahmed"]
print(student_name)
print(len(student_name))
print(student_name[0])

#Lists are declared similar to arrays in C
#Lists can store multiple types of data, but are generally used for homogenous ones.
#printing lists prints comma-separated list items surrounded by []
#individual values can be printed by selecting appropriate index

#Lists can be nested too
student_data=[["Shaun", 18], ["Linh", 20], ["Ahmed", 19]]
print(student_data)
print(student_data[0])
print(student_data[0][0])
print(len(student_data))

#List Comprehension
a=[i for i in range(1,11)]                          #creates a list that contain numbers from 1 to 10

#List Methods                                       #methods are the functions of class list
student_name.append("Mark")                         #appends one element to the last
student_data.extend([["Mark", 17], ["Steve", 21]])  #appends two or more elements to the last
student_name.insert(3, "Steve")                     #inserts to particular index
student_name.pop()                                  #remove last element
student_data.remove(["Mark", 17])                   #remove a particular element

print(student_data)
print(student_name)


print(a.count(3))                                   #returns number of instances of argument
print(a.index(3))                                   #returns index of the element specified
a.sort(reverse=True)                                #sorts list in descending order. sorts acseding if there are no arguments
print(a)
b=a.copy()                                          #returns a copy of a
print(b)
b.clear()                                           #removes all the elements from the list
print(b)

print(student_data[1:3])                            #prints from index 1 to 2
print(student_data[:2])                             #prints from starting index till 1st
print(student_data[2:])                             #prints from 2nd index till last
print(student_data[-3:-1])                          #prints from 3rd index from last till 1st index from last

#List Functions                                     #functions take the list as an argument
b=sorted(a)                                         #returns sorted copy of a, but a is not affected
print(a)
print(b)
print(len(a))                                       #returns number of elements of list
print(a.__sizeof__())                               #returns size occupied in bits
print(max(a))                                       #returns maximum value of list
print(min(a))                                       #returns minimum value of list
print(list(enumerate(student_name)))                #returns a list of enumerations of list elementss
print(student_name)

#List Operations
list1=[1,2,3]
list2=[4,5,6]
print(list1+list2)                                  #returns concatenation of list1&list2
print(list1*3)                                      #returns list repeated 3 times
f=int(input())
if f in list1: print("The element is present")      #returns a boolean, true or false
else: print("Element is absent")

#printing lists together
import itertools
name=['A', 'B', 'C']
age=[10,20,30]
course=['python','database']
length=[len(name), len(age), len(course)]
print(max(length))
for i in range(max(length)):
    if(len(name)>i):
        print(name[i])
    if(len(age)>i):
        print(age[i])
    if(len(course)>i):
        print(course[i])
#Gives Same output as
for i,j,k in itertools.zip_longest(name,age,course): print(i,j,k)
#shall import a library intertools for that
