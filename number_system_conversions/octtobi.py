oct = raw_input("enter an octal number with commas between each digit :")
x = oct.split(',')
l = len(x)
a = 0
Z = []
print "binary :",
while a!=l:
 b = []
 c =[]
 r = x[a]
 while r!=0:
  z = int(r)%2
  r = int(r)/2
  b.append(z)
 while len(b)%3!=0:
  b.append(0)
 l1 = len(b)
 d=0
 while d!=l1:
  c.append(b[l1-1-d])
  d=d+1
 print c,
 a=a+1
