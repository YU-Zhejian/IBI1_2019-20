#!/usr/bin/env python
# Get a number
#x=2019
x=int(input("Write number below 2^14 here:"))
o=str(x)+" is "
# Calculate from 2^13
n=13
# To 2^0
while (n>=0):
    if (2**n<=x):
        # print(str(2**n)+"<="+str(x))
        x=x-2**n
        # Modify the output
        o=o+"2**"+str(n)+"+"
    n=n-1
#Get ioutput and remove the ending "+"
print(str(o)[:-1])
