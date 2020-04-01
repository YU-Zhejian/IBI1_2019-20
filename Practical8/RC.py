#!/bin/env python
seq = 'ATGCGACTACGATCGAGGGCCAT'
seq_rev=seq[::-1]
rc=''
for seq_chr in seq_rev:
    if seq_chr=='A':
        rc = rc + 'T'
    elif seq_chr=='T':
        rc = rc + 'A'
    elif seq_chr=='C':
        rc = rc + 'G'
    else:
        rc = rc+ 'C'
print(rc)
