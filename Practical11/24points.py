#!/usr/env python
import sys

raw_str = input(r"Please input numbers to compute 24: (use ',' to divide them)")
num = []
for item in raw_str.split(","):
    num.append(float(item))
for item in num:
    if ((item > 23) or (item < 1)):
        print("Invalid number " + str(item) + ", which should have been between integers 1 to 23.")
        sys.exit(1)


# Replicate
def select_replicate():
    return ()


# List all possible situations
def select_calc(l: int):
    return_list = []
    il = list(range(l))
    for i in il:
        jl = il.copy()
        jl.pop(i)
        for j in jl:
            for k in range(4):
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

def select_copy(l: list):
    l_copy = l.copy()
    if len(l_copy) == len(sci) - 1:
        all_sit.append(l_copy)
    for item in sci[len(l)]:
        l.append(item)
        select_copy(l)
        l.pop()

select_copy([])

# Apply
def select_apply(i:int, j:int, k:int, l:list):
    if (k == 0):
        out = l[i] + l[j]
    elif (k == 1):
        out = l[i] - l[j]
    elif (k == 2):
        out = l[i] * l[j]
    else:
        out = l[i] / l[j]
    if (out == 24):
        return (0)
    else:
        l[i] = out
        l.pop(j)
        return (1)


n = 1
for item in all_sit:
    num_copy=num.copy()
    for jtem in item:
        if (select_apply(jtem[0], jtem[1], jtem[2], num_copy) == 0):
            print("Yes")
            print("Time: " + str(n))
            sys.exit(0)
        else:
            n = n + 1
print("No")
sys.exit(1)
