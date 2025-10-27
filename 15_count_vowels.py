#!/usr/bin/env python3
"""
Assignment 15: Count Vowels
Count vowels in a string (aeiou) and return counts per vowel.
"""

from collections import Counter

def count_vowels(s):
    s = s.lower()
    vowels = "aeiou"
    return {v: s.count(v) for v in vowels}

if __name__ == "__main__":
    print(count_vowels("This is a sample sentence."))
