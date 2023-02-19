'''
#Pickling
    changing a object into bytestream to transport its
    data across applications

#Unpickling
    decoding the bytestream into data
'''
import pickle

class St:
    def __init__(self, name, age, roll):
        self.name= name
        self.age= age
        self.roll= roll
    def info(self):
        print(self.name, self.age, self.roll)


lst= ['a', 'b', 'c', 'd', 'e']
st1= St('abc', 19, 1)
st2= St('def', 18, 2)
with open('a.txt', 'wb') as fh:
    #pickle.dump(lst, fh)        #encodes object and writes to file
    pickle.dump(st1, fh)
    pickle.dump(st2, fh)
with open('a.txt', 'rb') as fh:
    data= pickle.load(fh)       #decodes file into object
    data.info()
    data= pickle.load(fh)
    data.info()

'''
the file can be opened using another python file also, not only
in this one, but the data type should exist there also.
    eg. when class objects are passed, decoding is not easily
    possible to decode without knowing the class schema
'''
