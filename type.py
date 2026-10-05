while True:
 num=input('give integer: ')
 if num.isdigit(): 
     break
 else:
     print('Pls enter you number again')
 
num=int(num)
if num>=97 and num<=100:
    print('A+')
elif num>=93 and num<=96:
    print('A')
elif num>=90 and num<=92:
    print('A-')
elif num >=87 and num <=89:
    print('B+')
elif num>=80 and num<=82:
    print('B')
elif num>= 76 and num<=79:
    print('C+')
else:
       print('U R FAIL !!')

#diget is 0-9
#number ifinity