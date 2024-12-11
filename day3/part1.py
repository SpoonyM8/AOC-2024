#!/usr/bin/env python3
import re

def fromFile():
    with open('./puzzleInput.txt') as f:
        return "".join(line.rstrip() for line in f)

def sol():
    lines = fromFile()
    pattern = re.compile(r'mul\((\d+),(\d+)\)')
    total = 0
    for a, b in re.findall(pattern, lines):
        total += int(a) * int(b)
    return total
print(sol())