n, w= tuple(input().split())
n= int(n)
w= int(w)
mid= int(n/2)
des= ".|."
for i in range(n):
    des= des+".|."
j=0
if n>5 and n<101 and w== n*3:
    for i in range(n):
        if i<mid:
            j+=1
            print(des[:(i*6)+3].center(w,'-'))
        elif i==mid:
            print("WELCOME".center(w,'-'))
        else:
            j-=1
            print(des[:(j*6)+3].center(w,'-'))
