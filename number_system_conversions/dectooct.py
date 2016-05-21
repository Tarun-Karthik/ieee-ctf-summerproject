decimal = input("enter a decimal number :")
x = decimal
a = []
while x!=0:
 a.append(x%8)
 x=x/8
b = []
l = len(a)
q = 0
while q!=l:
 b.append(a[l-1])
 l=l-1

print b 
