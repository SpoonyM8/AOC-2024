#!/usr/bin/env python3

def lines():
    with open('./puzzleInput.txt') as f:
        return [line.rstrip() for line in f]

def lists():
    strippedLines = lines()
    leftList = []
    rightList = []
    for line in strippedLines:
        l, r = line.split('  ')
        leftList.append(int(l.strip()))
        rightList.append(int(r.strip()))
    leftList.sort()
    rightList.sort()
    return leftList, rightList

def sol():
    leftList, rightList = lists()

    s = 0
    for idx, num in enumerate(leftList):
        s = s + abs(num - rightList[idx])
    return s
print(sol())