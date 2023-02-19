#Exception Handling
try:
    #this is the block where exception handling code is kept
    print(x)    #raises error as 'x' is not declared
except TypeError:
    #this will be excecuted if there is a TypeError
    print("Type of 'x' is undefined")
except:
    #this will be excecuted if there is any other, it might be a long chain as if, elif, else 
    print('Something else went wrong')
else:
    #this will be excecuted if there is no error
    print('Nothing went wrong')
finally:
    #this wiil be excecuted if there is an error or not
    print('try-except is completed')
