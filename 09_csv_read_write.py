#!/usr/bin/env python3
"""
Assignment 09: CSV Read/Write
Write a list of dicts to CSV and read it back using csv.DictWriter/DictReader.
"""

import csv

def write_csv(path, rows, fieldnames):
    with open(path, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def read_csv(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))

if __name__ == "__main__":
    rows = [{"name":"Alice","age":30},{"name":"Bob","age":25}]
    fn = ["name","age"]
    write_csv("people.csv", rows, fn)
    print(read_csv("people.csv"))
