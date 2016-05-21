binary = raw_input("enter binary digits with a comma after each digit :")
x = binary.split(',')
l = len(x)
d = 0
y = []
while d!=l:
 y.append(x[l-1-d])
 d = d + 1
while len(y)%3!=0:
 y.append('0')
z = []
e = 0
l1 = len(y)
while e!=l1:
 z.append(y[l1-1-e])
 e = e + 1
a = 0

while a!=len(z):
 b = []
 f = a
 v = 0
 while v!=3:
   b.append(z[f])
   f = f + 1
   v = v + 1   
 g = 0
 j = 0
 while g!=3:
  k = int(b[2-g]) * (2**g)
  j = j +  k
  g = g + 1
 print j,
 a = a + 3
    
  
