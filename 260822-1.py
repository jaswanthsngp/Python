import itertools
#1
a=[]
n=int(input())
for i in range(n): a.append(input())
a.remove('')
print(a)

#2
a=[]
n=int(input())
for i in range(n): a.append(input())
x=input()
if(x in a):
    a.remove(x)
    print(a)
else: print("Element is absent in the list")

#3
tupleA=("This", "is", "a", 'python', 'lecture')
s=''
for i in tupleA: s=s+i+' '
print(s)

#4
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
#data=name+age+course
#for i in data: print(i)

#5
s1={1,2,3,4,5}
s2={4,5,6,7,8}
tupleS=tuple(s1.symmetric_difference(s2))
print(tupleS)
print((s1-s2)^(s2-s1))
