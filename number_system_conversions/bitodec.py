
binary = raw_input("enter a binary number with \' , \' after each digit :")
x = binary.split(',')
l = len(x)

a = 0
y = 0

while a != (l):
 z = int(x[l-1-a]) * (2**a)
 y = y + z
 a = a + 1


 
print "decimal form of the binary %s is %s" %(binary,y)