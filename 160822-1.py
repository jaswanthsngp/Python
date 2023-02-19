num= [23,43,56,10,3,72]
Max=0
for i in range(len(num)):
    if num[i]>Max: Max=num[i]
print(Max)

squarelist=[]
for i in range(1,11):squarelist.append(i*i)
print(squarelist)


name=input()
name=name.capitalize()
friends=['Aman', 'Shiv', 'Ram', 'Adam']
if name in friends: print('He is a friend')
else: print('Not a friend')

ident="python programming"
print(ident[2:4])           
print(ident[:5])
print(ident[5:])
print(ident[-3:-1])

age=[15, 36,24,10,12,43]
fr_details=[f"My friend is {i} years old" for i in age]
print(fr_details)
