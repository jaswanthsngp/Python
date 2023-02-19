weekends=(6, 7, 13, 14, 20, 21, 27, 28)
i=0
t=int(input())
for i in range(t):
    j=0
    holidays= 8
    n=int(input())
    a=list(map(int, input().split()))
    for j in range(n):
        if a[j] not in weekends:
            holidays= holidays+1
    print(holidays)
