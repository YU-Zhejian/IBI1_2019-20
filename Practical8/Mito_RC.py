#!/bin/env python
import re

myfasta=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r")
M_seq=re.findall(r'(>.*?:Mito:.*[AGCT\n]+?)>',myfasta.read())
myfasta.close()

out_seq=[]
outfasta=open(input("Type the name of new FASTA here:>"),"w")
for seq in M_seq:
    seq=seq.replace('\n','')
    seq=re.sub(r'>[^AGCT].*]',"> "+re.findall(r'gene:Q[\d]*',seq)[0]+" gene_length:"+str(seq.count("A")+seq.count("G")+seq.count("C")+seq.count("T"))+"\n",seq)+"\n"
    rev_str=re.findall(r'([AGCT]+)',seq)[0][::-1].translate(str.maketrans("AGCT","TCGA"))
    outfasta.write(re.sub(r'([AGCT]+)',rev_str,seq))
outfasta.close()
