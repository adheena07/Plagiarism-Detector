#!/usr/bin/env python3
"""
Assignment 05: Fibonacci Generator
Yield first n Fibonacci numbers using generator.
"""

def fib(n):
    a,b = 0,1
    for _ in range(n):
        yield a
        a,b = b, a+b

if __name__ == "__main__":
    print(list(fib(10)))
