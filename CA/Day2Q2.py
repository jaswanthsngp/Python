t=int(input())
for i in range(t):
    s= list(map(int, input().split()))
    if s[0]%s[1]==0: print(1)
    else: print(s[0]%s[1])
