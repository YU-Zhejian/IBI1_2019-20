#!/bin/env python
a=789
b=789789
if (b%7==0):
    print(str(b),"can be devided by 7")
else:
    print(str(b),"cannot be devided by 7")
c=b//7
d=c//11
e=d//13
print(str(c)+str(d)+str(e))
if (e>a):
    print("e>a")
elif (e<a):
    print("e<a")
else:
    print("e=a")
X=True
Y=True
Z=(X and not Y) or (Y and not X)
W=(X!=Y)
if (Z==W):
    print("Z=W")
else:
    print("Z!=W")
