#!/bin/env pthon
# Start with an int.
#n=1234
n=int(input("Write starting number here:"))
print(str(n))
#Loop until n=1
while (n!=1):
    # If n is even, divide by 2
    if (n%2==0):
        # It seems that using //instead of / can stop those dots.
        n=n//2
    # manipulate by 3 and add 1 if not
    else:
        n=n*3+1
    print(str(n))
