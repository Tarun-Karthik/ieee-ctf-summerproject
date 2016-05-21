hex = raw_input("enter an octal number with commas between each digit :")
x = hex.split(',')
l = len(x)
a = 0
Z = []
print "binary :",
while a!=l:
 b = []
 c =[]
 if x[a]=='A':
  r=10
 elif x[a]=='B':
  r=11
 elif x[a]=='C':
  r=12
 elif x[a]=='D':
  r=13
 elif x[a]=='E':
  r=14
 elif x[a]=='F':
  r=15
 else:
  r = x[a]
 while r!=0:
  z = int(r)%2
  r = int(r)/2
  b.append(z)
 while len(b)%4!=0:
  b.append(0)
 l1 = len(b)
 d=0
 while d!=l1:
  c.append(b[l1-1-d])
  d=d+1
 print c,
 a=a+1
