#!/usr/bin/env python3
"""
Assignment 12: Quicksort (in-place Lomuto partition)
"""

def quicksort(a, lo=0, hi=None):
    if hi is None: hi = len(a)-1
    if lo < hi:
        p = partition(a, lo, hi)
        quicksort(a, lo, p-1)
        quicksort(a, p+1, hi)

def partition(a, lo, hi):
    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    return i

if __name__ == "__main__":
    arr = [3,6,8,10,1,2,1]
    quicksort(arr)
    print(arr)
