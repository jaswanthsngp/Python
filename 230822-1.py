a=[]
n=int(input())
for i in range(n): a.append(int(input()))
b=[(i,a[i]) for i in range(n)]
print(b)

c={2, 6, 4, 6, 8}
d={1,2,3,4}
c.intersection_update(d)
e=list(c)
print(e)
