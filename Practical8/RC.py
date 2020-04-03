#!/bin/env python
seq = 'ATGCGACTACGATCGAGGGCCAT'
seq_rev=seq[::-1]
print(seq_rev.translate(str.maketrans("AGCT","TCGA")))
