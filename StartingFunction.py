#!/usr/bin/python

from __future__ import division
from __future__ import print_function

# Homework Thursday February 05
# Starting function

# define the function
def get_at_content(dna):
    length = len(dna)
    a_count = dna.count('A')
    t_count = dna.count('T')
    at_content = (a_count + t_count) / length
    return at_content

# provide the data    
##dna = "ATTGTCGGGGCTT"
##dna = "TTTT"
##dna = "ATGCGCGATCGATCGAATCG"
##dna = "ATGCATGCAACTGTAGC"
dna = "aactgtagctagctagcagcgta"

# print the results to the screen
print(get_at_content(dna))
