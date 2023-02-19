#Sets
    #Unordered
    #No duplicates allowed
a={1,20,4,2,1,4,5}
print(a)
#print(a[0])                        #values of sets can't be accessed through index, as they are unordered
print(type(a))
b={}                                #empty sets can't be declared like this.
print(b)
print(type(b))                      #it results in empty dictionary
b=set()
print(type(b))                      #set() fn gives an empty set
b={1}
print(b)                            #Sets can be with single or multiple values 
for i in a: print(i)                #foreach loop can be used to print values of set

    #methods
#difference_update, intersection_update, symmetric_difference
a={10,20,1,2,25,26}
b={3,73,45,10,92}
d={10}
e=set(a)
b.add(2)                            #adds an element to the set
print(b)
b.remove(2)                         #removes particular element, returns error if the element is absent
print(b)
b.pop()                             #removes any random element
print(b)
b.discard(25)                       #removes particular elemnt, doesn't return error even if element is absent
print(b)
c=a.union(b)                        #returns union of a and b
print(c)
c=a.difference(b)                   #returns differnce of a and b
print(c)
c=a.intersection(b)                 #returns intersection of a and b
print(c)
print(a.isdisjoint(b))              #returns boolean, is disjoint or not
print(a.issubset(d))                #returns if a is subset of d
print(a.issuperset(d))              #returns if a is superset of d
a.difference_update(d)              #removes common elements from a
print(a)
a.add(10)
a.intersection_update(d)            #removes uncommon elements from a
print(a)
print(b.symmetric_difference(d))    #returns a set with uncommon elements


    #functions
#len, sorted, max, min, sum, enumerate
print(len(e))
print(sorted(e))
print(max(e))
print(min(e))
print(sum(e))
c=enumerate(d)
print(c)

    #operations

a={10,20,1,2,25,26}
b={3,73,45,10,92}
c=a|b                               #a or b
print(c)
c=a&b                               #a and b
print(c)
c=a-b
print(c)
print(a>=b)                         #returns boolean if a is superset to b
print(a<=b)                         #returns boolean if a is subset to b
c=a^b                               #returns a U b
print(c)
print(10 in a)                      #returns if element is present in a
print(10 not in a)

#|, &, -, =>, <=, ^, in, not in
