#!/usr/bin/env python3
"""
Assignment 19: Sieve of Eratosthenes
Return list of primes <= n.
"""

def sieve(n):
    if n < 2: return []
    is_prime = [True]*(n+1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p*p <= n:
        if is_prime[p]:
            for k in range(p*p, n+1, p):
                is_prime[k] = False
        p += 1
    return [i for i,ok in enumerate(is_prime) if ok]

if __name__ == "__main__":
    print(sieve(50))
