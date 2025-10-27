#!/usr/bin/env python3
"""
Assignment 18: Graph DFS (recursive)
Given adjacency list dict, perform DFS and return visitation order.
"""

def dfs(graph, start):
    visited = set()
    order = []
    def _dfs(u):
        visited.add(u)
        order.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                _dfs(v)
    _dfs(start)
    return order

if __name__ == "__main__":
    g = {"A":["B","C"], "B":["D"], "C":[],"D":[]}
    print(dfs(g,"A"))
