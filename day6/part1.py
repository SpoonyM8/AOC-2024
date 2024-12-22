#!/usr/bin/env python3

def linesFromFile():
    with open('./puzzleInput.txt') as f:
        return [line.rstrip() for line in f]

def isSafeIndices(row, col, numRows, numCols):
    return row >= 0 and row < numRows and col >= 0 and col < numCols

def originalPos(board, numRows, numCols):
    for row in range(0, numRows):
        for col in range(0, numCols):
            if board[row][col] == '^':
                return [row, col]

def fillVisited(numRows, numCols):
    visited = []
    for row in range(0, numRows):
        newRow = []
        for col in range(0, numCols):
            newRow.append(False)
        visited.append(newRow)
    return visited

moves = {
    0: [-1, 0],
    1: [0, 1],
    2: [1, 0],
    3: [0, -1]
}

def solve():
    board = linesFromFile()
    numRows = len(board)
    numCols = len(board[0])
    [currRow, currCol] = originalPos(board, numRows, numCols)
    
    currMove = 0
    visited = fillVisited(numRows, numCols)

    while(True):
        move = moves[currMove]
        rowChange = move[0]
        colChange = move[1]
        newRow = currRow + rowChange
        newCol = currCol + colChange

        if not isSafeIndices(newRow, newCol, numRows, numCols):
            break

        if board[newRow][newCol] == '#':
            currMove = 0 if currMove == 3 else currMove + 1
        else:
            visited[currRow][currCol] = True
            currRow = newRow
            currCol = newCol


    count = 0
    for row in range(0, numRows):
        for col in range(0, numCols):
            if visited[row][col]:
               count += 1
    print(count + 1)
        
    
solve()    