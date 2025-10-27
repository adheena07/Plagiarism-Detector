#!/usr/bin/env python3
"""
Assignment 08: File Word Count
Count words in a UTF-8 text file and print top 10 most common words.
"""

from collections import Counter
import re

def count_words_in_file(path):
    with open(path, encoding="utf-8") as f:
        text = f.read().lower()
    words = re.findall(r"\b[a-z']+\b", text)
    return Counter(words)

if __name__ == "__main__":
    # create a sample file and count
    sample = "sample_text.txt"
    with open(sample, "w", encoding="utf-8") as f:
        f.write("This is a sample text. This text is simple. This is sample.")
    c = count_words_in_file(sample)
    print(c.most_common(10))
