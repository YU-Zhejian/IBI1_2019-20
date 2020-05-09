#!/usr/env python
import sys
import math
raw_str = input(r"Please input numbers to compute 24: (use ',' to divide them)")
num = []
for item in raw_str.split(","):
    num.append(float(item))
for item in num:
    if ((item > 23) or (item < 1)):
        print("Invalid number " + str(item) + ", which should have been between integers 1 to 23.")
        sys.exit(1)
# List all possible situations
def select_calc(l: int) -> list:
    '''
    This function is designed to list all the operations available with l cards. These operations are represented as [index of operation number 1, index of operation number 2. operation].
    :param l: The number of cards.
    :return: A list consisting all possible operation lists.
    '''
    return_list = []
    for i in list(range(l - 1)):
        for j in list(range(i + 1, l)):
            for k in range(6):
                return_list.append([i, j, k])
    return (return_list)
sc = [[], []]
for i in range(2, len(num) + 1):
    sc.append(select_calc(i))
all_sit = []
all_sit_tmp = []
sci = []
for i in range(len(num)):
    sci.append(sc[len(num) - i])
# Select one operation [] from one stage.
def select_apply(i: int, j: int, k: int, l: list):
    if k == 0:
        out = l[i] + l[j]
    elif k == 1:
        out = l[i] - l[j]
    elif k == 2:
        out = l[j] - l[i]
    elif k == 3:
        out = l[i] * l[j]
    elif k == 4:
        if(l[j] != 0):
            out = l[i] / l[j]
        else:
            return (1)
    else:
        if l[i] != 0:
            out = l[j] / l[i]
        else:
            return(1)
    if (out == 24):
        return (0)
    else:
        l[i] = out
        l.pop(j)
        return (1)
def select_copy(l: list):
    '''
    :param l: a list of all operation steps.
    :return: NONE
    '''
    global all_sit
    global n
    l_copy = l.copy()
    if len(l_copy) == len(sci) - 1:
        num_copy = num.copy()
        for jtem in l_copy:
            if (select_apply(jtem[0], jtem[1], jtem[2], num_copy) == 0):
                print("Yes")
                l=len(num)
                print("Recursion Times: " + str(n)+"/"+str((4**(l-1))*math.factorial(l)*(math.factorial(l-1))))
                sys.exit(0)
            else:
                n = n + 1
    for item in sci[len(l)]:
        l.append(item)
        select_copy(l)
        l.pop()
# Apply
n=1
select_copy([])
print("No")
sys.exit(1)
