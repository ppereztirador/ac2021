import numpy as np
dataList = []
window = 3

with open('input') as fh:
    for line in fh:
        dataList.append(int(line))

# What's the last sample that I can include in a full window
lastSample = int(len(dataList)/window) * window # With int's!!
windowedData = np.zeros(lastSample)

for ii in range(window):
    windowedData += dataList[ii:lastSample+ii]

dataDiff = np.diff(windowedData)
print(np.sum(dataDiff>0))
