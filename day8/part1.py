#!/usr/bin/env python3

def linesFromFile():
    with open('./puzzleInput.txt') as f:
        return [line.rstrip() for line in f]

def isSafeIndices(row, col):
    return row >= 0 and row < 50 and col >= 0 and col < 50

lines = linesFromFile()
antinodes = set()
def addAntinodes(row, col):
    node = lines[row][col]
    for rowNum in range(0,50):
        for colNum in range(0,50):
            if (lines[rowNum][colNum] == node and (row != rowNum or col != colNum)):
                nodeRowNum = 2 * rowNum - row
                nodeColNum = 2 * colNum - col
                if (isSafeIndices(nodeRowNum, nodeColNum)):
                    antinodes.add((nodeRowNum, nodeColNum))

def solve():
    for rowNum in range(0,50):
        for colNum in range(0,50):
            if (lines[rowNum][colNum] != '.'):
                addAntinodes(rowNum, colNum)

    print(len(antinodes))        

solve()    