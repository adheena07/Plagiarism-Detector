#!/usr/bin/env python3
"""
Assignment 10: Binary Search
Implement iterative binary search returning index or -1.
"""

def binary_search(a, target):
    lo, hi = 0, len(a)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if a[mid] == target:
            return mid
        if a[mid] < target:
            lo = mid+1
        else:
            hi = mid-1
    return -1

if __name__ == "__main__":
    arr = [1,3,5,7,9]
    print(binary_search(arr, 7), binary_search(arr, 2))
