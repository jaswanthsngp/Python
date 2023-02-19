string= input()

with open('a.txt', 'w') as f:
    f.write(string)
with open('a.txt', 'r') as f:
    inp= f.read()
    l1= inp.split()
print(l1)
