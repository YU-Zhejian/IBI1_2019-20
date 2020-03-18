#!/bin/env python
import matplotlib.pyplot as plt
dna="ATGCTTCAGAAAGGTCTTACG"
dna_dict={'A':0,'T':0,'C':0,'G':0}

for n in range(0,len(dna)):
    dna_dict[dna[n:n+1]]=dna_dict[dna[n:n+1]]+1

dna_list=[0,0,0,0]
dna_list[0]=dna_dict['A']
dna_list[1]=dna_dict['T']
dna_list[2]=dna_dict['C']
dna_list[3]=dna_dict['G']

for dna_key in dna_dict:
    print(dna_key+"="+str(dna_dict[dna_key]))
lbl='A','T','C','G'
plt.pie(dna_list,labels=lbl,autopct='%1.1f%%')
plt.axis('equal')
plt.title('pie for the four DNA nucleotides.')
plt.show()
