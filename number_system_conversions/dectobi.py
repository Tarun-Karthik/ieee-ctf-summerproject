x = raw_input("enter a decimal number  :")
decimal = x
y = []
z = []
if x=='1':
  z.append(1)
else:
  while 1:
   b = int(x) % 2
   y.append(b)
   x=int(x)/2
   if x== 1:
    break
   
 
if decimal != '1': 
  y.append(x)
  
l = len(y)
a = l
l=l-1
if decimal != '1':
  while True:
   z.append(y[l])
   l=l-1
   if len(z) == a:
     break
 
print"binary of %s is %s" %(decimal,z)
