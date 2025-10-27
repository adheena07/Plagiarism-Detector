#!/usr/bin/env python3
"""
Assignment 11: Merge Sort
Implement merge sort (return new sorted list).
"""

def merge_sort(a):
    if len(a) <= 1: return list(a)
    mid = len(a)//2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    i=j=0; out=[]
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i+=1
        else:
            out.append(right[j]); j+=1
    out.extend(left[i:]); out.extend(right[j:])
    return out

if __name__ == "__main__":
    print(merge_sort([5,2,9,1,5,6]))
