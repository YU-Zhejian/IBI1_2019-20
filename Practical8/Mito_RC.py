#!/bin/env python
import re
outfasta=input("Type the name of new FASTA here:>")
myfasta=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r")
record=False
out_seq = []
out_seq_tmp = ""
for seq in myfasta:
    if re.search(r'^>.*',seq):
        if out_seq_tmp != '':
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

out_rc = []
for seq in out_seq:
    seq_rev=seq[::-1]
    rc=''
    if re.search(r'^>.*',seq):
        rc=seq
    else:
        for seq_chr in seq_rev:
            if seq_chr=='A':
                rc = rc + 'T'
            elif seq_chr=='T':
                rc = rc + 'A'
            elif seq_chr=='C':
                rc = rc + 'G'
            else:
                rc = rc+ 'C'
        rc=rc+'\n'
    out_rc.append(rc)

outfasta=open(outfasta,"w")
for seq in out_rc:
    outfasta.write(seq)
outfasta.close()