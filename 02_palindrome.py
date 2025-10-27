#!/usr/bin/env python3
"""
Assignment 02: Palindrome Checker
Check whether a string is palindrome (ignore non-alphanumerics and case).
"""

import re

def is_palindrome(s):
    s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return s == s[::-1]

if __name__ == "__main__":
    samples = ["A man, a plan, a canal: Panama", "hello", "Madam"]
    for s in samples:
        print(f"{s!r} ->", is_palindrome(s))
