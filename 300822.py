a= {}
sq={}
l1=['n1', 'n2', 'n3']
l2=[1, 2, 3]
for i in range(len(l1)): a[l1[i]]=l2[i]
print(a)
a1={'key1':2, 'key2': 45}
a.update(a1)
print(a)

sq={x:x*x for x in range(10)}
print(sq)
