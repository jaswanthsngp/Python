#Logical Operators

x= int(input("Enter any  positive number: "))
number_above= x==20 or x>20         # "or" keyword is used to represent logical OR
print (number_above)
number_between= x>0 and x<20        # "and" keyword is used to represent logical AND
print(number_between)
number_neg= not x>0                 # "not" keyword is used to represent logical NOT or Negation
print(number_neg)
