#!/bin/env python
#Get data
import matplotlib.pyplot as plt
#dna="ATGCTTCAGAAAGGTCTTACG"
dna=input("Write sequence here:")
dna_dict={'A':0,'T':0,'C':0,'G':0}

#Add to dictionary
for n in dna:
    dna_dict[n]=dna_dict[n]+1

#Enumerate dictionary
for dna_key in dna_dict:
    print(dna_key+"="+str(dna_dict[dna_key]))

#Transcribe the dictionary to a list, whcih may be used by plt.
dna_list=[0,0,0,0]
dna_list[0]=dna_dict['A']
dna_list[1]=dna_dict['T']
dna_list[2]=dna_dict['C']
dna_list[3]=dna_dict['G']

#Plot the fata
lbl='A','T','C','G'
plt.pie(dna_list,labels=lbl,autopct='%1.1f%%')
plt.axis('equal')
plt.title('pie for the four DNA nucleotides.')
plt.show()
