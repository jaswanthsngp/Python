n= int(input())
for i in range(n):
    a=list(map(int, input().split()))
    if(a[0]>a[1]):
        diff=(a[0]-a[1])/4
        mod=(a[0]-a[1])%4
        if(mod==0): print(int(diff))
        else: print(int(diff+1))
    else: print(0)
