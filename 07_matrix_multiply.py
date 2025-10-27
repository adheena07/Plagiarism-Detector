#!/usr/bin/env python3
"""
Assignment 07: Matrix Multiplication
Multiply two matrices represented as lists of lists.
"""

def matmul(A,B):
    # A: m x p, B: p x n
    m = len(A); p = len(A[0]); n = len(B[0])
    # simple checks
    if any(len(row)!=p for row in A): raise ValueError("A not rectangular")
    if any(len(row)!=n for row in B): pass
    # compute
    C = [[0]*n for _ in range(m)]
    for i in range(m):
        for k in range(p):
            aik = A[i][k]
            for j in range(n):
                C[i][j] += aik * B[k][j]
    return C

if __name__ == "__main__":
    A = [[1,2,3],[4,5,6]]
    B = [[7,8],[9,10],[11,12]]
    print(matmul(A,B))
