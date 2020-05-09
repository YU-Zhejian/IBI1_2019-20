#!/bin/env python
import re
import os
os.chdir("D:\\Smst2\\IBI1B\\IBI1_2019-20\\Practical8")
myfasta=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r")
M_seq=re.findall(r'(>.*?:Mito:.*[AGCT\n]+?)>',myfasta.read())
myfasta.close()
out_seq=[]
outfasta=open(input("Type the name of new FASTA here:>"),"w")
for seq in M_seq:
    lines= list(seq.split('\n'))
    seq_head=lines[0]
    seq_def = ''.join(lines[1:]).replace('\n', '').translate(str.maketrans("AGCT","TCGA"))[::-1]
    head='> '+re.findall(r'Q[\d]*',seq_head)[0]+' '+str(len(seq_def))
    outfasta.write(head+'\n'+seq_def+'\n')
outfasta.close()
