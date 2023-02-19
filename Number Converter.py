#Number converter

n= input('Enter the number ')
c= int(input('The number is a\n1.Decimal\n2.Binary\n3.Octal\n4.Hexadecimal\n'))
if c==1:
    n= int(n)
elif c==2:
    n= int(n, 2)
elif c==3:
    n= int(n, 8)
elif c==4:
    n= int(n, 16)
else:
    print('Invalid Input')

if c>0 and c<5:
    c= int(input('You want to convert it to\n1.Decimal\n2.Binary\n3.Octal\n4.Hexadecimal\n'))
    if c==1:
        print('Its Decimal form is', n)
    elif c==2:
        print('Its Binary form is', str(bin(n)[2:]))
    elif c==3:
        print('Its Octal form is', str(oct(n))[2:])
    elif c==4:
        print('Its Hexadecimal form is', str(hex(n))[2:])
    else:
        print('Invalid Input')
