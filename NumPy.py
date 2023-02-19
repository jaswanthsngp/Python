#NumPy
import numpy as np
l1= [12, 10, 5, 23, 70]
nparr= np.array(l1)             #this method is used to convert list/tuple into numpy array
print(nparr)
nparr= np.array((12,10,5,23))
print(nparr)
print(nparr.dtype)              #datatype of elements in it
print(nparr.shape)              
print(nparr.size)               
print(nparr.ndim)               #dimension of array
x= np.zeros((2,5), dtype=int)   #an array filled with '0's, default dtype is float
print(x)
x= np.ones((2,5))
print(x)
x= np.full((2,5),25)            #an array filled with given value
print(x)
x= np.arange(2,10,3)            #range between 2 and 10 with a gap of 3
print(x)
#x=linspace(1,5)
#print(x)
x= np.identity(5)               #an identity matrix of order 5
print(x)
x= np.array([[1,2,3], [4,5,6]]) #an matrix of two rows
print(x)
print(x.sum(axis= 0))           #sums of elements on same columns
print(x.sum(axis= 1))           #sums of elements on same rows
path= open('a.txt', mode= 'r')
x= np.loadtxt(path, dtype=int, delimiter=' ')
print(x)                        #reads data from file, seperates on the basis of delimiter
