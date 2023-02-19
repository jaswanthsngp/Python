#File Handling
#no special header required as in C/C++
'''
    Text File:
        Stores data as strings
        opened in text mode
    Binary File:
        Stores data in binary form
        openend in binary mode
'''

f= open("student.txt", "w")             #Opens/Creates 'student.txt' in write mode
f.write('Hello\n')                      #writes into 'student.txt' in the form of string
f.write('Welcome to file handling')
print(f)
print(f.name)
print(f.readable())
f.close()

f= open("student.txt", 'r')             #Opens 'student.txt' in read mode
data= f.read()                          #returns data in the file
print(data)
f.close()

f= open('student.txt', 'rb')            #opens student.txt in binary read mode
data= f.read()                          #it prints all the charachters as they are
print(data)                             #binary files are not decoded, and hence
f.close()                               #printed as they are

f= open("student.txt", 'w')
l= ['a', 'b', 'c', 'd', 'e']
f.writelines(l)                         #writes list elements directly, one item after another,
f.close()                               #with no space between any

f= open('student.txt', 'a')             #append mode, pointer points to the last index of file
for i in l:
    f.write(f'\n{i}{i}')
f.close()

f= open('student.txt', 'r')
print(f.tell())                         #returns the position of file pointer, starts at 0 in read/write mode
data= f.read(14)
print(data)
print(f.tell())
f.seek(5)
print(f.tell())
data= f.read(5)
print(data)
print(f.tell())
f.close()
