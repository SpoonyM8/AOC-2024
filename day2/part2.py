#!/usr/bin/env python3

def lines():
    with open('./puzzleInput.txt') as f:
        return [line.rstrip() for line in f]

def reports():
    strippedLines = lines()
    formattedReports = []

    for report in strippedLines:
        levels = [int(level) for level in report.split(' ')]
        formattedReports.append(levels)

    return formattedReports

def isSafe(report):
    isIncreasing = report[0] < report[1]
    isDecreasing = not isIncreasing
    for idx, lvl in enumerate(report):
        if (idx == len(report) - 1):
            return True
        nextLvl = report[idx+1]
        diff = abs(lvl - nextLvl)
        if ((isIncreasing and lvl >= nextLvl) or (isDecreasing and lvl <= nextLvl) or (diff < 1 or diff > 3)):
            return False
    return True

def sol():
    formattedReports = reports()
    safeCount = 0
    for report in formattedReports:
        if (isSafe(report)):
            safeCount += 1
            continue
        isReportSafe = False    
        for idx in range(0, len(report)):
            if isSafe(report[:idx] + report[idx+1:]):
                isReportSafe = True
        if (isReportSafe):
            safeCount += 1

    return safeCount
print(sol())