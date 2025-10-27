#!/usr/bin/env python3
"""
Assignment 04: Custom Sort
Implement an insertion sort (in-place) for a list of numbers.
"""

def insertion_sort(a):
    a = list(a)
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

if __name__ == "__main__":
    arr = [5,2,9,1,5,6]
    print("Before:", arr)
    print("After: ", insertion_sort(arr))
