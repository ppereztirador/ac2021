import numpy as np

axisList = []
amountList = []

decideAxis = lambda x: [1,0] if x=='forward' else [0,1] if x=='down' else [0,-1]

with open('input') as fh:
    for line in fh:
        lineParse = line.split(' ')
        axisList.append(decideAxis(lineParse[0]))
        amountList.append(int(lineParse[1]))

aim = 0
hPos = 0
depth = 0

for i in range(len(amountList)):
    aim += amountList[i] * axisList[i][1]
    hPos += amountList[i] * axisList[i][0]
    depth += amountList[i] * aim * axisList[i][0]

print(hPos * depth)
