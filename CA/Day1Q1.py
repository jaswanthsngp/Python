x=int(input())+5
balance= float(input())
if x>0 and x<=5000 and balance>=0 and balance<=5000:
    if x%5==0 and balance>=x: balance=balance-x
    print(round(balance, 2))
