from itertools import combinations as com
c=0;
d={}
for i in range (26):
    d[chr(97+i)]=i+1;
n,l= list(map(int, input().split()))
for i in com(d.keys(),n):
             s=0
             for j in i: s+=d[j]
             if(s==l): c+=1
print(c)
