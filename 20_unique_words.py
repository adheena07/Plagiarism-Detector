#!/usr/bin/env python3
"""
Assignment 20: Unique Words Preserving Order
Return list of unique words from a sentence preserving first occurrence order.
"""

def unique_words(sentence):
    seen = set(); out = []
    for w in sentence.split():
        if w not in seen:
            seen.add(w); out.append(w)
    return out

if __name__ == "__main__":
    print(unique_words("this is a test this is only a test"))
