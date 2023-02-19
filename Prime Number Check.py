#For loop

n=int(input("Enter any number: "))
c=i=0
for i in range(2,n):
    if n%i==0:
        c=c+1
        print(i," ")
    i=i+1
if c>0: print("Are the factors of",n)
else: print(n,"is a prime number")
