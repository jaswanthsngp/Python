#make all elements in a list unique
def unique(l1):
    l2=[]
    for i in l1:
        if i not in l2: l2.append(i)
    #l2= list(set(l1))
    return l2
print(unique([2, 3, 3, 2, 5]))

#reverse the digits of a 4 digit number
def reverse(x):
    a=int(x/1000)
    x=x%1000
    b=int(x/100)
    x=x%100
    c=int(x/10)
    x=x%10
    y=x*1000+c*100+b*10+a
    return y;
print(reverse(1234))

#add alternate elemets of the list
def sumalt(l1):
    sume=0
    for i in range(len(l1)):
        if i%2==0: sume=sume+l1[i]
    return sume
print(sumalt([1, 2, 3, 4, 5, 6]))
