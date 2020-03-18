#!/bin/env python
import matplotlib.pyplot as plt
gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]

gene_lengths.sort()
gene_lengths=gene_lengths[1:len(gene_lengths)-1]

plt.boxplot(gene_lengths,labels=["Gene"])
plt.title("Gene length distribution")
plt.show()
