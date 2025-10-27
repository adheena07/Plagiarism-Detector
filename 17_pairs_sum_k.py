#!/usr/bin/env python3
"""
Assignment 17: Find pairs with sum K
Given list and K, return list of unique pairs (a,b) with a<=b and a+b==K.
"""

def pairs_with_sum(a, K):
    seen = set()
    pairs = set()
    for x in a:
        need = K - x
        if need in seen:
            pairs.add(tuple(sorted((x,need))))
        seen.add(x)
    return sorted(list(pairs))

if __name__ == "__main__":
    print(pairs_with_sum([1,2,3,4,3,2], 5))
