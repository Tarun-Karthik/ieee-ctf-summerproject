octal= raw_input("enter an octal number with a comma \',\' between each digit :")
x = octal.split(',')
b = 0
a = 0
l=len(x)
y=0

while a!=(l):
 z = int(x[l-1-a]) * (8**a)
 y = y + z
 a = a + 1
 
print "decimal form is %s :" %y