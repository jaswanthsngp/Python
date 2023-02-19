#Dictionaries
#empty dictionaries can be diclared as a={}
#syntax to declare dictionaries
a={
    'A': 20,
    'B': 30,
    'C': 40
   }
print(a['A'])           #accessing data: dict_name[key_name], but returns 'Key exception' if key is absent
print(a.get('A'))       #get method is error proof, returns 'None' in the absence of key
print(type(a))
print(a)
a={}                    #dictionaries can be empty too
print(a)

#a list of tuples with paired values can be converted into list
a=dict([('a', 1), ('b',2), ('c',3)])
print(a)
student= {'name': 'xyz', 'age': 26, 'course': ['Python', 'Operating System']}
#print(student[roll])       #Raises an error as there is no key named roll
print(student.get('roll'))  #Returns 'None' in the absence of key
student['name']= 'ABC'      #Updates existing key
student['roll']= 12         #Creates new key, if not existing
student.update({'reg': 121, 'section': 'K21GP'})    #Update method is used to add/update multiple keys
print(student)

for i in student: print(i,student[i])       #raw method to print keys and values
for i in student.keys(): print(i)           #keys() method returns keys
for i in student.values(): print(i)         #values() method returns values of keys
for i in student.items(): print(i)          #items() method returns key and value pairs in a touple
for i, j in student.items(): print(i,j)

#Dictionary Methods
st=student.copy()                           #returns a copy of the dictionary
print(st)
print(st.pop('section'))                    #removes key and its values and returns removed values
print(st.popitem())                         #removes the last item and returns it
print(st)
print(a.fromkeys('abc'))                    #assingns default values
print(a)
print(st)
del(st['age'])                              #deletes particular key and values, does not return anything
print(st)
st.clear()                                  #clears all data of dictionary
print(st)

