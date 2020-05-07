#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
plt . figure(figsize=(6,4),dpi =150)
S=9999
I=1
R=0
N=S+I+R
beta=0.3
gamma=0.05
s=[S]
i=[I]
r=[R]
time=1000
for tmp in range(1,time+1):
    curr_beta=beta*I/N
    s_inf=list(np.random.choice(range(2),S,p=[1-curr_beta,curr_beta])).count(1)
    S=S-s_inf
    I=I+s_inf
    i_rec=list(np.random.choice(range(2),I,p=[1-gamma,gamma])).count(1)
    I=I-i_rec
    R=R+i_rec
    s.append(S)
    i.append(I)
    r.append(R)
plt.xlabel('time')
plt.ylabel('population')
plt.title('SIR model')
plt.plot(list(range(time+1)), s, 'b',label='Susceptible')
plt.plot(list(range(time+1)), i, 'r',label='Infected')
plt.plot(list(range(time+1)), r, 'g',label='Recovered')
legend = plt.legend(loc='upper right', shadow=True, fontsize='x-large')
plt.savefig("SIR",type='png')
plt.close()
