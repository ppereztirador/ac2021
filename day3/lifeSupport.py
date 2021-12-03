import numpy as np

listValues = []
with open('input') as fh:
    for line in fh:
        listValues.append(list(map(int,line[:-1]))) # -1 to skip \n

listValues = np.array(listValues)

bitConversion = 2 ** np.arange(listValues.shape[1]-1, -1, -1)

listIndices = [True]*listValues.shape[0]
listRefined = listValues[listIndices,:]
for i in range(listValues.shape[1]):
    more1s_priority1 = np.sum(listRefined[:,i])>=(int(listRefined.shape[0])/2)
    listIndices = more1s_priority1==listRefined[:,i]
    listRefined = listRefined[listIndices]
    if len(listRefined)<=1: break

oxygen = listRefined[0]

listIndices = [True]*listValues.shape[0]
listRefined = listValues[listIndices,:]
for i in range(listValues.shape[1]):
    more0s_priority0 = np.sum(listRefined[:,i])<(int(listRefined.shape[0])/2)
    listIndices = more0s_priority0==listRefined[:,i]
    listRefined = listRefined[listIndices]
    if len(listRefined)<=1: break

co2 = listRefined[0]

oxygenInt = np.sum(bitConversion * oxygen)
co2Int = np.sum(bitConversion * co2)

print(oxygenInt, co2Int, oxygenInt * co2Int)
