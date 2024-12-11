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
    rightMap = {}
    leftList, rightList = lists()
    for num in rightList:
        rightMap[num] = rightMap.get(num, 0) + 1

    leftList, rightList = lists()

    s = 0
    for num in leftList:
        s = s + (num * rightMap.get(num, 0))

    return s

print(sol())