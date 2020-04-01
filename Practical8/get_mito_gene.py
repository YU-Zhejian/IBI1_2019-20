#!/bin/env python
import re
myfasta=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r")
record=False
out_seq = []
out_seq_tmp = ""
for seq in myfasta:
    if re.search(r'^>.*',seq):
        if out_seq_tmp != '':
            out_seq_tmp=out_seq_tmp+"\n"
            out_seq.append(out_seq_tmp)
            out_seq_tmp=""
        if re.search(r'^>.*_mRNA cdna chromosome:R64-1-1:Mito.*',seq):
            record=True
            out_seq.append(seq)
        else:
            record=False
    elif record:
        out_seq_tmp=out_seq_tmp+seq.strip()
myfasta.close()

outfasta=open("mito_gene.fa","w")
for seq in out_seq:
    outfasta.write(seq)
outfasta.close()