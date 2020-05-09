#!/usr/bin/env python
seq = 'ATGCGACTACGATCGAGGGCCAT'
print(seq.translate(str.maketrans("AGCT","TCGA"))[::-1])
