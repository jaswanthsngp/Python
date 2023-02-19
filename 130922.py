#Class Student to take and dispaly a student's data
'''class Student:
    def __init__(self, n, a, s):
        self.name= n
        self.age= a
        self.section= s
    def display(self):
        print(f"{self.name} aged {self.age} years belongs to {self.section}")    
st1= Student('name1', 19, 'K21GP')
st2= Student('name2', 18, 'K21GP')
st3= Student('name3', 20, 'K21GP')
st1.display()
st2.display()
st3.display()'''

#Class BankAccount to deposit, withdraw and display money available
'''class BankAccount():
    def __init__(self, b):
        self.balance= b
    def deposit(self, a):
        self.balance= self.balance+a
    def withdraw(self, a):
        self.balance= self.balance-a
    def amount(self):
        print("Balance availiable:", self.balance)
acc= BankAccount(5000)
acc.deposit(500)
acc.amount()
acc.withdraw(200)
acc.amount()'''

#Function to check whether the braces are closed or not, in correct order
#pending
def bracketCheck(st):
    lc=0
    rc=0
    ls=0
    rs=0
    lp=0
    rp=0
    for i in range(len(st)):
        if st[i]=='{':
            lc+=1
            for 
        if st[i]=='}': rc+=1
        if st[i]=='[': ls+=1
        if st[i]==']': rs+=1
        if st[i]=='(': lp+=1
        if st[i]==')': rp+=1
    if lc>rc: print(f"{lc-rc} Right Curly brackets are missing")
    elif rc>lc: print(f"{rc-lc} Right Curly brackets are extra")
    if ls>rs: print(f"{ls-rs} Right Square brackets are missing")
    elif rs>ls: print(f"{rs-ls} Right Square brackets are extra")
    if lp>rp: print(f"{lp-rp} Right parantheses are missing")
    elif rp>lp: print(f"{rp-lp} Right parantheses are extra")
s= input()
bracketCheck(s)
