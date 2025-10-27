#!/usr/bin/env python3
"""
Assignment 14: Reverse Words in Sentence
Given a sentence, reverse the order of words (preserve word chars).
"""

def reverse_words(sentence):
    parts = sentence.split()
    return " ".join(reversed(parts))

if __name__ == "__main__":
    s = "Hello world this is Python"
    print(reverse_words(s))
