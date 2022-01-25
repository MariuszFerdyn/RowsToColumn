#!/usr/bin/env python3

import csv
import sys

fileName = sys.argv[1]

try:
    c1 = int(sys.argv[2]) - 1
except IndexError:
    c1 = 0

try:
    c2 = int(sys.argv[3]) - 1
except IndexError:
    c2 = 1

try:
    skip = int(sys.argv[4])
except IndexError:
    skip = 0

with open(fileName, newline='') as f:
    reader = csv.reader(f)
    skipped = 0
    key = ''
    result = list()
    columnsList = {}
    rowInProgress = dict()
    for row in reader:
        if skipped < skip:
            skipped += 1
            continue
        if key == '':
            key = row[c1]
        if row[c1] == key:
            if rowInProgress:
                result.append(rowInProgress)
            rowInProgress = dict()
        columnsList[row[c1]] = ''
        rowInProgress[row[c1]] = row[c2]
    result.append(rowInProgress)

print(','.join(columnsList.keys()))
for i in result:
    row = []
    for c in columnsList.keys():
        try:
            row.append(i[c])
        except KeyError:
            row.append('')
    print(','.join(row))
