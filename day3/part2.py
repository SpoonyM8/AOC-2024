#!/usr/bin/env python3
import re

def fromFile():
    with open('./puzzleInput.txt') as f:
        return "".join(line.rstrip() for line in f)

def sol():
    lines = fromFile()
    pattern = re.compile(r'mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))')
    total = 0
    enabled = True
    for a, b, do, dont in re.findall(pattern, lines):
        if do:
            enabled = True
        if dont:
            enabled = False
        if enabled and a and b:
            total += int(a) * int(b)
    return total
print(sol())