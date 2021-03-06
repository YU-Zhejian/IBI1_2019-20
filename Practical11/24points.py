#!/usr/bin/env python
from math import factorial
from tqdm import tqdm
raw_str = input(r"Please input numbers to compute 24: (use ',' to divide them)")
num = []
for item in raw_str.split(","):
    try:
        fi=float(item)
    except:
        exit(1)
    if ((fi > 23) or (fi < 1)):
        print("Invalid number " + str(item) + ", which should have been between integers 1 to 23.")
        exit(1)
    num.append(fi)
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
            return 2
    else:
        if l[i] != 0:
            out = l[j] / l[i]
        else:
            return 2
    if (out == 24):
        return 0
    else:
        l[i] = out
        l.pop(j)
        return 1
def select_copy(l: list):
    '''
    :param l: a list of all operation steps.
    :return: NONE
    '''
    global pbar
    l_copy = l.copy()
    if len(l_copy) == len(sci) - 1:
        num_copy = num.copy()
        for jtem in l_copy:
            sa=select_apply(jtem[0], jtem[1], jtem[2], num_copy)
            if sa==0:
                return 1
            elif sa==2:
                return 2
            else:
                pbar.update(1)
    for item in sci[len(l)]:
        l.append(item)
        sc_ret=select_copy(l)
        if 1==sc_ret:
            return sc_ret
        l.pop()
# Apply
l=len(num)
el=3**(l-1)*(l-1)*factorial(l)*factorial(l-1)
with tqdm(total=el) as pbar:
    sc_ret = select_copy([])
    rect=pbar.format_dict['n']
    pbar.close()
    del pbar
    if 1==sc_ret:
        print("Yes")
    else:
        print("No")
print("Recursion Times:"+str(rect)+"/"+str(el))
