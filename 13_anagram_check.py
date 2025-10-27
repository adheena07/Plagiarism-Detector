#!/usr/bin/env python3
"""
Assignment 13: Anagram Check
Return True if two strings are anagrams (ignore spaces and case).
"""

from collections import Counter
import re

def are_anagrams(a,b):
    pattern = re.compile(r'[^A-Za-z0-9]')
    a = pattern.sub('', a).lower()
    b = pattern.sub('', b).lower()
    return Counter(a) == Counter(b)

if __name__ == "__main__":
    print(are_anagrams("listen", "silent"))
    print(are_anagrams("Dormitory", "Dirty room"))
