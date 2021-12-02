import numpy as np
dataList = []

with open('input') as fh:
    for line in fh:
        dataList.append(int(line))

dataDiff = np.diff(dataList)
print(np.sum(dataDiff>0))
