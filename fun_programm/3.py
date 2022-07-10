#!/bin/python3 
import telnetlib 
tn = telnetlib.Telnet("35.193.60.121" , 1337) 
def bobfav(n):
    for i in range (int(n/1856)):
        if (n - (i*1856)) % 2014 == 0 :
            return True
    return False
while (True):
    a = tn.read_until(b"Answer:")
    print((a))
    if b"Good" in a :
        n =  int(a.spilt()[2])
    else:
        n =  int(a.spilt()[0])
        if bobfav(n):
            tn.write(b"Yes\n")
        else:
            tn.write(b"Yes\n")

