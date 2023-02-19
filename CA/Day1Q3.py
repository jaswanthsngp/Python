t=int(input())
if t>0 and t<201:
    for i in range(t):
        h=int(input())
        if h>0 and h<169:
            if h<=10: c= 50
            else: c=50+10*(h-10)
            print(c)
