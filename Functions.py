#functions
def message():                                      #Functions are defined using 'def' keyword
    name= input("Enter a name ")
    print(f"Hello, {name}")
message()
#print(name)                                        #gives error, as the var 'name' is defined to the scope of function only

student={'name': 'ABD', 'section': 'K21GP', 'marks': 78}

def student_details(student):                       #no need to define the datatypes when passing argument
    n=student['name']
    m=student['marks']
    print(f"The student {n} scored {m} marks")
student_details(student)

def demo(*args): print(args)                        #using '*' before argument name allows to take multiple arguments, later combined to a list/tuple

demo('one', 'two', 'three')

def demo(**kwargs): print(kwargs)                   #using '**' before argument name allows to take multiple arguments with keys, i.e. as dicts
demo(First="one", second='two', third= 'three')

def is_even(x):                                     #no need to define return type when returning a value
    if x%2==0: return True
    else: return False
print(is_even(4))

