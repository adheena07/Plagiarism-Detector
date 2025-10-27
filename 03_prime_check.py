#!/usr/bin/env python3
"""
Assignment 03: Prime Check
Efficiently check if n is prime (trial division up to sqrt(n)).
"""

import math

def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0: return False
    r = int(math.isqrt(n))
    for i in range(3, r+1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    for x in [1,2,3,4,16,17,97,100]:
        print(x, is_prime(x))
