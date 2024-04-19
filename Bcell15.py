#!/usr/bin/env python3
"""EPITOPE SEARCH.

Performs a sliding window operation on sequence 1 and looks for each
kmer on sequence 2.
Outputs a .txt file containing the sequences analised, the matching
kmers found and the number of times each kmer was found in each comparison.
file1 and file2 are the ones to be compared.
w_size is given as the maximum size to be run, and it will decrease with each
run until a set stopping parameter.

author: alvaro salgado
salgado.alvaro@me.com
"""

import numpy as np
import pandas as pd
import re
import sys

# Sliding window size
w_size = int(15)

# Opens .csv files containing sequences to be compared, in a pandas DataFrame.
# Each .csv file contains one sequence per line.
# Column of interest is denoted 'epitopo'
data_1_df = pd.read_csv("MHC2overlap.csv", sep=';')
data_2_df = pd.read_csv("BcellPrepared.csv", sep=';')
epitopes_1 = data_1_df['epitopo']
epitopes_2 = data_2_df['epitopo']


# Save results in a numpy array, to be later converted into a .txt file.
# result contains epitopes 1, 2, kmer found, size and number of times found.
result = np.empty((0, 5), str)
result = np.append(result,
                   np.array([['epitope_1', 'epitope_2', 'kmer', 'size', 'times']]),
                   axis=0)

# Resuces window size until 2
while w_size > 1:
    # For each epitope in data_2
    for epit_2 in epitopes_2:
        # For each position in epit_2 (i.e., sliding window)
        for i in range(len(epit_2)-w_size+1):
            # Gets one kmer for each step of the sliding window.
            kmer = epit_2[i:(i+w_size)]
            # Looks for this kmer in each epitope in data_1
            for epit_1 in epitopes_1:
                searchObj = re.findall(kmer, epit_1)
                n = len(searchObj)
                # If kmer is found, appends a new line to result containing.
                if n > 0:
                    result = np.append(result,
                                       np.array([[epit_1, epit_2, kmer, len(kmer), n]]),
                                       axis=0)
    output = "%s_%s_%s_out.txt" % ("MHC2overlap.csv", "BcellPrepared.csv", w_size)
    out = open(output, "w+")
    np.savetxt(output, result, fmt='%s', delimiter=',')
    out.close()
    w_size -= 1
    result = np.empty((0, 5), str)
    result = np.append(result,
                       np.array([['epitope_1', 'epitope_2', 'kmer', 'size', 'times']]),
                       axis=0)


############################################################################
### MAIN
############################################################################
# file1 = 'b_cells_shared.csv'
# file2 = 'ctl_shared.csv'
# w_size = 3
# i = 1
# epit_1 = epitopes_1[0]
# epit_2 = epitopes_2[0]
