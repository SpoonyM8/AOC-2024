#!/usr/bin/env python3

def linesFromFile():
    with open('./puzzleInput.txt') as f:
        return [line.rstrip() for line in f]

def sol():
    lines = linesFromFile()
    numOccurences = 0

    for row in range(0, 138):
        for col in range(0, 138):
                firstDiag = lines[row][col] + lines[row+1][col+1] + lines[row+2][col+2]
                secondDiag = lines[row][col+2] + lines[row+1][col+1] + lines[row+2][col]
                if (firstDiag == 'SAM' or firstDiag == 'MAS') and (secondDiag == 'MAS' or secondDiag == 'SAM'):
                    numOccurences += 1

    return numOccurences
print(sol())