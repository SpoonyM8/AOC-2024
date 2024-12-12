#!/usr/bin/env python3

def linesFromFile():
    with open('./puzzleInput.txt') as f:
        return [line.rstrip() for line in f]

def isSafeIndices(row, col):
    return row >= 0 and row <= 139 and col >= 0 and col <= 139

def numXmas(row, col, lines):
    # find X
    if (lines[row][col] != 'X'):
        return False
    # find M
    total = 0
    m = []
    rowDir, colDir = 0,0
    for rowGuess in range(row-1, row+2):
        for colGuess in range(col-1, col+2):
            if not isSafeIndices(rowGuess, colGuess):
                continue
            if lines[rowGuess][colGuess] == 'M':
                rowDir = rowGuess - row
                colDir = colGuess - col
                d = {}
                d['rowDir'] = rowDir
                d['colDir'] = colDir
                d['pos'] = [rowGuess, colGuess]
                m.append(d)
    
    for mPos in m:
        # find A
        aRowGuess = mPos['pos'][0] + mPos['rowDir']
        aColGuess = mPos['pos'][1] + mPos['colDir']
        if not isSafeIndices(aRowGuess, aColGuess):
            continue
        if lines[aRowGuess][aColGuess] != 'A':
            continue

        # find S
        sRowGuess = mPos['pos'][0] + (2 * mPos['rowDir'])
        sColGuess = mPos['pos'][1] + (2 * mPos['colDir'])
        if not isSafeIndices(sRowGuess, sColGuess):
            continue
        if lines[sRowGuess][sColGuess] == 'S':
            total = total + 1
    return total 

def sol():
    lines = linesFromFile()
    numOccurences = 0

    for row in range(0, 140):
        for col in range(0, 140):
            numOccurences = numOccurences + numXmas(row, col, lines)

    return numOccurences
print(sol())