#!/usr/bin/env python3
"""
Assignment 01: Factorial
Write a function factorial(n) that returns n! for n>=0 (use iteration).
"""

def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

if __name__ == "__main__":
    import sys
    n = int(sys.argv[1]) if len(sys.argv)>1 else 5
    print(f"{n}! =", factorial(n))
