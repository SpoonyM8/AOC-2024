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
                multiplier = 0
                rowDiff = rowNum - row
                colDiff = colNum - col

                nodeRowNum = rowNum + multiplier * rowDiff
                nodeColNum = colNum + multiplier * colDiff
                while (isSafeIndices(nodeRowNum, nodeColNum)):
                    antinodes.add((nodeRowNum, nodeColNum))
                    multiplier += 1
                    nodeRowNum = rowNum + multiplier * rowDiff
                    nodeColNum = colNum + multiplier * colDiff

def solve():
    for rowNum in range(0,50):
        for colNum in range(0,50):
            if (lines[rowNum][colNum] != '.'):
                addAntinodes(rowNum, colNum)
    print(len(antinodes))        

solve()    