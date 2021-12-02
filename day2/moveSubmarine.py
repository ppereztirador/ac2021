import numpy as np

axisList = []
amountList = []

decideAxis = lambda x: [1,0] if x=='forward' else [0,1] if x=='down' else [0,-1]

with open('input') as fh:
    for line in fh:
        lineParse = line.split(' ')
        axisList.append(decideAxis(lineParse[0]))
        amountList.append(int(lineParse[1]))

moveArray = np.array(axisList) * np.tile(amountList, (2,1)).T
moveTotal = np.sum(moveArray, axis=0)

print(moveTotal[0]*moveTotal[1])
