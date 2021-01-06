a,b,c = 123, 3.4567, 3.4+1.2j
print (a)
print (b)
print (c)
print (a,b,c)
print (a,)
print (b,c)
print ("a=",a, " b=",b, " c=", c)
print ("a=%d, b=%f, c=%f+%fi" %(a,b,c.real,c.imag))
print ("a=%d, b=%.2f, c=%.2f+%.2fi" %(a,b,c.real,c.imag))
print ("%10d" %(a))
print ("%010d" %(a))
print ("%-10defg" %(a))
print ("%-010defg" %(a))
print ("%1d" %(a))
print ("%*d" %(10,a))

num=171
print ('%d = %#o = %#x' % (num,num,num))
print ('%10d' %(num))
print ('%-10def' %(123))

st="Computer"
print ('%s' %(st))
print ('%.3s' %(st))

for i in range(1,8):
    print ("%.*s" %(i,st))

bno=0b101011; octno=0o123; hexno=0x1ab
print(bno, octno, hexno)
print("Binary: %d,%d,%d" %(bno, octno, hexno))
print("Hexadecimal: %x,%x,%x" %(bno, octno, hexno))
print("Octal: %o,%o,%o" %(bno, octno, hexno))
print("Hexadecimal: %#x,%#x,%#x" %(bno, octno, hexno))
print("Octal: %#o,%#o,%#o" %(bno, octno, hexno))

    

