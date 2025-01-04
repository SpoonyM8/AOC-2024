#!/usr/bin/env python3

def linesFromFile():
    with open('./puzzleInput.txt') as f:
        return [line.rstrip() for line in f]

def isSafeIndices(row, col, numRows, numCols):
    return row >= 0 and row < numRows and col >= 0 and col < numCols

def isValidTestVal(testVal, nums, total):
    if (len(nums) == 0):
        return False
    
    addTotal = nums[0] + nums[1] if total == 0 else total + nums[0]
    prodTotal = nums[0] * nums[1] if total == 0 else total * nums[0]
    concatTotal = int(str(nums[0]) + str(nums[1])) if total == 0 else int(str(total) + str(nums[0]))
    remainingNums = nums[2:] if total == 0 else nums[1:]

    if ((addTotal == testVal or prodTotal == testVal or concatTotal == testVal) and len(remainingNums) == 0):
        return True

    return isValidTestVal(testVal, remainingNums, addTotal) or isValidTestVal(testVal, remainingNums, prodTotal) or isValidTestVal(testVal, remainingNums, concatTotal)

def solve():
    ans = 0

    for line in linesFromFile():
        inp = line.split(':')
        testVal = int(inp[0])
        nums = [int(num) for num in inp[1].strip().split(' ')]
        if (isValidTestVal(testVal, nums, 0)):
            ans += testVal
    print(ans)        

solve()    