#!/usr/bin/env python3
"""
Assignment 16: Simple Calculator Class
Implement a Calculator class with add, sub, mul, div methods.
"""

class Calculator:
    def add(self, a,b): return a+b
    def sub(self, a,b): return a-b
    def mul(self, a,b): return a*b
    def div(self, a,b):
        if b == 0: raise ZeroDivisionError("division by zero")
        return a/b

if __name__ == "__main__":
    c = Calculator()
    print(c.add(5,3), c.sub(5,3), c.mul(5,3), c.div(5,3))
