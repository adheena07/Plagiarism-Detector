#!/usr/bin/env python3
"""
Assignment 06: GCD and LCM
Write functions gcd(a,b) and lcm(a,b).
"""

def gcd(a,b):
    a,b = abs(a), abs(b)
    while b:
        a,b = b, a%b
    return a

def lcm(a,b):
    if a == 0 or b == 0: return 0
    return abs(a//gcd(a,b)*b)

if __name__ == "__main__":
    print("gcd(48,18) =", gcd(48,18))
    print("lcm(48,18) =", lcm(48,18))
