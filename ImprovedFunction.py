#!/usr/bin/python

from __future__ import division
from __future__ import print_function

# Homework Thursday February 05
# Improved function

# define the function
# add significant figures argument
def get_at_content(dna, sig_figs):
    
    # convert N's to upper case and remove them
    dna = dna.upper().replace('N','')
    length = len(dna)
    
    # convert to upper case
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    # use the round() function to specify significant figures
    return round(at_content, sig_figs)

# provide the data    
##dna = "ATTGTCGGGGCTT"
##dna = "TTTT"
##dna = "ATGCGCGATCGATCGAATCG"
##dna = "ATGCATGCAACTGTAGC"
##dna = "aactgtagctagctagcagcgta"
##dna = "TTCGNNN"
dna = "tnnacgnnat"

# specify significant figures
##sig_figs = 2
sig_figs = 3
##sig_figs = 4

# print the results to the screen
print(get_at_content(dna, sig_figs))
