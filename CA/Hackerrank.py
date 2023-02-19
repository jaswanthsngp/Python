from collections import namedtuple

n= int(input())
scheme= input()
#print(scheme)
marksheetlist= []
scheme= scheme.split()
#print(scheme)
markloc= -1
marklist= []
for i in range(4):
    if scheme[i]== 'MARKS':
        markloc= i
for i in range(n):
    marksheetlist.append(input().split())
    #print(marksheetlist[i])
    marklist.append(float(marksheetlist[i][markloc]))
#print(marklist)
result= round(sum(marklist)/len(marklist))
print('{0:.2f}'.format(result))
