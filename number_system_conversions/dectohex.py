decimal = input("enter a  number :")
x = decimal
a = []
while x!=0:
 if (x%16)==10:
  a.append('A')
 elif (x%16)==11:
  a.append('B')
 elif (x%16)==12:
  a.append('C')
 elif (x%16)==13:
  a.append('D')
 elif (x%16)==14:
  a.append('E')
 elif (x%16)==15:
  a.append('F')
 else:
  a.append(x%16)
 x=x/16
b = []
l = len(a)
q = 0
while q!=l:
 b.append(a[l-1])
 l=l-1

print b 
