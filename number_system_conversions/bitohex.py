binary = raw_input("enter binary digits with a comma after each digit :")
x = binary.split(',')
l = len(x)
d = 0
y = []
while d!=l:
 y.append(x[l-1-d])
 d = d + 1
while len(y)%4!=0:
 y.append('0')
z = []
e = 0
l1 = len(y)
while e!=l1:
 z.append(y[l1-1-e])
 e = e + 1
a = 0
print z
while a!=len(z):
 b = []
 f = a
 v = 0
 while v!=4:
   b.append(z[f])
   f = f + 1
   v = v + 1   
 g = 0
 j = 0
 while g!=4:
  k = int(b[3-g]) * (2**g)
  j = j +  k
  g = g + 1
 if j==10:
   print 'A',
 elif j==11:
   print 'B',
 elif j==12:
   print 'C',
 elif j==13:
   print 'D',
 elif j==14:
   print 'E',
 elif j==15:
   print 'F',
 else:
   print j,
 a = a + 4