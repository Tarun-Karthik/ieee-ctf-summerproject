hexadecimal= raw_input("enter an hexadecimal number with a comma \',\' between each digit :")
x = hexadecimal.split(',')
b = 0
a = 0
l=len(x)
y=0
while b!=l:
 if x[b]=='A':
   x[b]=10
 elif x[b]=='B':
   x[b]=11
 elif x[b]=='C':
   x[b]=12
 elif x[b]=='D':
   x[b]=13
 elif x[b]=='E':
   x[b]=14
 elif x[b]=='F':
   x[b]=15
 b=b+1
while a!=(l):
 z = int(x[l-1-a]) * (16**a)
 y = y + z
 a = a + 1
 
print "decimal form is %s :" %y
